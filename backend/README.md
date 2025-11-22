# Backend Server Setup

This is the Python Flask backend server for the Heart Attack Prediction API.

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python app.py
   ```
   
   Or use the startup script:
   ```bash
   python start.py
   ```

The server will start on `http://localhost:5000`

## API Endpoints

### POST/GET `/api/get`
Main prediction endpoint for heart attack risk prediction.

**Request Body (POST):**
```json
{
  "cholesterol": 200,
  "bp": 120,
  "diabetes": false,
  "obesity": false,
  "chest_pain": true,
  "shortness_of_breath": false,
  "stress": false,
  "poor_sleep": false,
  "smoking": false
}
```

**Response:**
```json
{
  "prediction": 0,
  "probability": 0.23,
  "risk_level": "Low"
}
```

### POST `/predict`
Legacy endpoint for compatibility with frontend.

### GET `/health`
Health check endpoint to verify server status.

## Notes

- The model will be trained automatically on first run if `src/heart.csv` exists
- If the CSV file is not found, a dummy model will be created for testing
- The trained model is saved to `src/heart_model.pkl` for faster startup on subsequent runs

