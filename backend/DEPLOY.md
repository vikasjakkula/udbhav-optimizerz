# Render.com Deployment

## Files Required:
- `api.py` - Main FastAPI application
- `heart_rf_model.joblib` - Trained model
- `scaler.joblib` - Data scaler
- `requirements.txt` - Python dependencies
- `Procfile` - Render.com startup command

## Render.com Setup:
1. Connect GitHub repo
2. Set root directory: `backend`
3. Build command: `pip install -r requirements.txt`
4. Start command: (auto-detected from Procfile)
5. Environment: Python 3

## Endpoints:
- Health: `/health`
- Predict: `/predict` (POST)
- Docs: `/docs`

