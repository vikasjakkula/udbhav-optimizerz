from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import joblib
import numpy as np

# Load model and scaler
try:
    model = joblib.load("heart_rf_model.joblib")
    scaler = joblib.load("scaler.joblib")
except FileNotFoundError as e:
    print(f"Warning: {e}")
    model = None
    scaler = None

# Numeric features used for scaling
numeric_features = [
    "age", "resting_blood_pressure", "cholesterol",
    "max_heart_rate_achieved", "st_depression"
]


class HeartInput(BaseModel):
    # Frontend form fields
    name: Optional[str] = None
    age: Optional[float] = None
    sex: Optional[int] = None
    cholesterol: Optional[float] = None
    bp: Optional[float] = None  # Blood pressure
    fbs: Optional[bool] = False  # Fasting blood sugar > 120
    thalachh: Optional[float] = None  # Max heart rate achieved
    diabetes: Optional[bool] = False
    obesity: Optional[bool] = False
    shortness_of_breath: Optional[bool] = False
    chest_pain: Optional[bool] = False
    sweating: Optional[bool] = False
    stress: Optional[bool] = False
    poor_sleep: Optional[bool] = False
    smoking: Optional[bool] = False
    
    # Allow model-specific fields as well for direct API calls
    resting_blood_pressure: Optional[float] = None
    max_heart_rate_achieved: Optional[float] = None
    st_depression: Optional[float] = None
    chest_pain_type: Optional[int] = None
    fasting_blood_sugar: Optional[int] = None
    resting_ecg: Optional[int] = None
    exercise_induced_angina: Optional[int] = None
    st_slope: Optional[int] = None
    num_major_vessels: Optional[int] = None
    thalassemia: Optional[int] = None


app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predicts heart disease risk using Random Forest",
    version="1.0"
)

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def map_frontend_to_model(frontend_data: dict) -> dict:
    """
    Map frontend form fields to model expected format
    """
    data = frontend_data.copy()
    
    # Map bp to resting_blood_pressure
    if data.get("bp") is not None and data.get("resting_blood_pressure") is None:
        data["resting_blood_pressure"] = data["bp"]
    
    # Map thalachh to max_heart_rate_achieved
    if data.get("thalachh") is not None and data.get("max_heart_rate_achieved") is None:
        data["max_heart_rate_achieved"] = data["thalachh"]
    
    # Map fbs boolean to fasting_blood_sugar int
    if data.get("fasting_blood_sugar") is None:
        data["fasting_blood_sugar"] = 1 if data.get("fbs", False) else 0
    
    # Map chest_pain boolean to chest_pain_type int
    if data.get("chest_pain_type") is None:
        # 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic
        data["chest_pain_type"] = 1 if data.get("chest_pain", False) else 2
    
    # Map shortness_of_breath to exercise_induced_angina
    if data.get("exercise_induced_angina") is None:
        data["exercise_induced_angina"] = 1 if data.get("shortness_of_breath", False) else 0
    
    # Default values for missing required fields
    defaults = {
        "age": 50.0,
        "resting_blood_pressure": 120.0,
        "cholesterol": 200.0,
        "max_heart_rate_achieved": 150.0,
        "st_depression": 0.0,
        "sex": 1,
        "chest_pain_type": 2,
        "fasting_blood_sugar": 0,
        "resting_ecg": 0,
        "exercise_induced_angina": 0,
        "st_slope": 1,
        "num_major_vessels": 0,
        "thalassemia": 2
    }
    
    # Apply defaults for missing fields
    for key, default_value in defaults.items():
        if data.get(key) is None:
            data[key] = default_value
    
    return data


@app.post("/predict")
def predict(patient: HeartInput):
    """
    Predict heart attack risk based on patient data
    Frontend expects: { probability: float } where probability is 0-1
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=500, detail="Model files not found. Please ensure heart_rf_model.joblib and scaler.joblib are in the directory.")
    
    try:
        patient_dict = patient.dict()
        
        # Map frontend fields to model format
        mapped_data = map_frontend_to_model(patient_dict)
        
        # Create DataFrame with model-expected columns in correct order
        # Model expects 13 features total: 5 numeric (scaled) + 8 categorical (unscaled)
        model_columns = [
            "age", "resting_blood_pressure", "cholesterol",
            "max_heart_rate_achieved", "st_depression",
            "sex", "chest_pain_type", "fasting_blood_sugar",
            "resting_ecg", "exercise_induced_angina",
            "st_slope", "num_major_vessels", "thalassemia"
        ]
        
        # Create DataFrame with correct column order and ensure all values are numeric
        df_data = {}
        for col in model_columns:
            value = mapped_data.get(col, 0)
            # Convert to float for numeric columns, int for categorical
            if col in numeric_features:
                df_data[col] = [float(value)]
            else:
                df_data[col] = [int(value)]
        
        df = pd.DataFrame(df_data, columns=model_columns)
        
        # Extract numeric features for scaling
        numeric_data = df[numeric_features].values
        
        # Scale only the numeric features
        scaled_numeric = scaler.transform(numeric_data)
        
        # Replace numeric features with scaled values in the DataFrame
        for i, feature in enumerate(numeric_features):
            df[feature] = scaled_numeric[:, i]
        
        # Ensure DataFrame has all 13 columns in correct order
        df_final = df[model_columns].copy()
        
        # Debug: Check DataFrame shape and columns
        if df_final.shape[1] != model.n_features_in_:
            raise HTTPException(
                status_code=500, 
                detail=f"Feature mismatch: DataFrame has {df_final.shape[1]} features, but model expects {model.n_features_in_} features. Columns: {list(df_final.columns)}"
            )
        
        # Predict using all 13 features
        prediction = int(model.predict(df_final)[0])
        probability_raw = model.predict_proba(df_final)[0][1]  # Probability of heart attack (0-1)
        probability_percent = round(probability_raw * 100, 2)
        
        # Return in format expected by frontend
        return {
            "probability": float(probability_raw),  # Frontend expects 0-1
            "prediction": prediction,
            "risk_percentage": probability_percent,
            "health_status": "High Risk" if prediction == 1 else "Low Risk"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.get("/health")
def health():
    """Health check endpoint"""
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
