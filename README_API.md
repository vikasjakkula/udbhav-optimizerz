# Heart Attack Prediction API

FastAPI server running on `localhost:5000`

## Quick Start

### Option 1: Run with Python (Recommended)
```powershell
python api.py
```

### Option 2: Run with Batch File
```powershell
.\START_API.bat
```

### Option 3: Run with Uvicorn directly
```powershell
uvicorn api:app --host 0.0.0.0 --port 5000 --reload
```

## Server Information

- **URL**: http://localhost:5000
- **Health Check**: http://localhost:5000/health
- **API Documentation**: http://localhost:5000/docs
- **Prediction Endpoint**: http://localhost:5000/predict (POST)

## API Endpoints

### POST /predict
Predict heart attack risk

**Request Body:**
```json
{
  "name": "John Doe",
  "age": 45,
  "sex": 1,
  "cholesterol": 200,
  "bp": 120,
  "fbs": false,
  "thalachh": 150,
  "diabetes": false,
  "chest_pain": false,
  "shortness_of_breath": false,
  "smoking": false
}
```

**Response:**
```json
{
  "probability": 0.23,
  "prediction": 0,
  "risk_percentage": 23.0,
  "health_status": "Low Risk"
}
```

### GET /health
Check server and model status

**Response:**
```json
{
  "status": "ok",
  "model_loaded": true,
  "scaler_loaded": true
}
```

## Requirements

Make sure you have the following files in the same directory:
- `api.py` (this file)
- `heart_rf_model.joblib` (trained model)
- `scaler.joblib` (data scaler)

## Dependencies

All required packages should be installed:
- fastapi
- uvicorn
- scikit-learn
- pandas
- joblib
- pydantic

## Troubleshooting

If you get "Module not found" errors:
```powershell
pip install fastapi uvicorn scikit-learn pandas joblib pydantic
```

If port 5000 is already in use:
- Stop any other application using port 5000
- Or change the port in `api.py` (line 183)

