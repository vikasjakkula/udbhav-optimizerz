from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os

app = Flask(__name__)
CORS(app)

# Global model variable
model = None

def load_or_train_model():
    """Load a saved model or train a new one"""
    global model
    
    model_path = 'src/heart_model.pkl'
    
    # Try to load existing model
    if os.path.exists(model_path):
        try:
            import pickle
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            print(f"Loaded existing model from {model_path}")
            return model
        except Exception as e:
            print(f"Error loading model: {e}. Will train a new one.")
    
    # Train new model
    print("Training new model...")
    
    # Load or use sample data structure
    # Note: In production, you should have the actual heart.csv file
    try:
        df = pd.read_csv('src/heart.csv')
    except FileNotFoundError:
        print("Warning: heart.csv not found. Creating a dummy model.")
        # Create a dummy model for testing
        model = LogisticRegression(solver='saga', penalty='l1', max_iter=1000)
        # Dummy training data structure
        X_dummy = np.random.rand(100, 11)  # 11 features
        y_dummy = np.random.randint(0, 2, 100)
        model.fit(X_dummy, y_dummy)
        return model
    
    # Data preprocessing - match the notebook's feature selection
    # Drop columns as per notebook: trtbps, thalachh, age, chol, sex, fbs, restecg, slp
    cols_to_drop = ['trtbps', 'thalachh', 'age', 'chol', 'sex', 'fbs', 'restecg', 'slp', 'output']
    # Only drop columns that exist
    cols_to_drop = [col for col in cols_to_drop if col in df.columns]
    
    X = df.drop(columns=cols_to_drop)
    y = df['output']
    
    print(f"Training model with features: {list(X.columns)}")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # Train model
    model = LogisticRegression(solver='saga', penalty='l1', multi_class='auto', max_iter=1000)
    model.fit(X_train, y_train)
    
    # Save model
    try:
        import pickle
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model saved to {model_path}")
    except Exception as e:
        print(f"Warning: Could not save model: {e}")
    
    return model

def map_frontend_to_model_data(form_data, model_columns):
    """
    Map frontend form data to model input format based on actual model columns
    
    Frontend sends:
    - cholesterol, bp, diabetes, obesity, shortness_of_breath, 
      chest_pain, sweating, stress, poor_sleep, smoking
    """
    # Initialize feature dictionary with defaults
    feature_dict = {}
    
    # Map frontend data to model features
    feature_dict['cp'] = 1 if form_data.get('chest_pain', False) else 2  # chest pain type
    feature_dict['exng'] = 1 if form_data.get('shortness_of_breath', False) else 0  # exercise induced angina
    feature_dict['oldpeak'] = 0.5 if form_data.get('stress', False) else 0.0  # ST depression
    smoking = form_data.get('smoking', False)
    feature_dict['caa'] = 1 if smoking else 0  # number of major vessels
    feature_dict['thall'] = 1 if smoking else 2  # thalium stress test result
    
    # Build feature array in the order the model expects
    features = []
    for col in model_columns:
        if col in feature_dict:
            features.append(feature_dict[col])
        else:
            # Default values for missing features
            features.append(0)
    
    return np.array(features).reshape(1, -1)

@app.route('/api/get', methods=['POST', 'GET'])
def predict():
    """API endpoint for heart attack prediction"""
    global model
    
    # Initialize model if not already loaded
    if model is None:
        model = load_or_train_model()
    
    try:
        if request.method == 'POST':
            data = request.get_json()
        else:
            # For GET requests, use query parameters
            data = request.args.to_dict()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Map frontend data to model input
        # Get the column names the model was trained on
        if hasattr(model, 'feature_names_in_'):
            model_columns = list(model.feature_names_in_)
        else:
            # Fallback: use common expected columns
            model_columns = ['cp', 'exng', 'oldpeak', 'caa', 'thall']
        input_features = map_frontend_to_model_data(data, model_columns)
        
        # Make prediction
        prediction = model.predict(input_features)[0]
        probability = model.predict_proba(input_features)[0][1]  # Probability of heart attack
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability),
            'risk_level': 'High' if probability > 0.6 else 'Medium' if probability > 0.3 else 'Low'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict_legacy():
    """Legacy endpoint for compatibility with frontend"""
    result = predict()
    # Adjust response format if needed
    if isinstance(result, tuple):
        response, status = result
        if status == 200:
            data = response.get_json()
            return jsonify({'probability': data.get('probability', 0)}), status
    return result

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'model_loaded': model is not None})

if __name__ == '__main__':
    # Load model on startup
    load_or_train_model()
    app.run(debug=True, host='0.0.0.0', port=5000)

