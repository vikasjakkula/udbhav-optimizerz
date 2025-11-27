@echo off
title Heart Attack Prediction API - Port 5000
color 0A
echo ========================================
echo  Heart Attack Prediction API Server
echo ========================================
echo.
echo Starting server on: http://localhost:5000
echo.
echo Endpoints:
echo   - Health Check: http://localhost:5000/health
echo   - API Docs:     http://localhost:5000/docs
echo   - Predict:      http://localhost:5000/predict (POST)
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.

python api.py

pause

