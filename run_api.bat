@echo off
title FastAPI Server - Port 5000
echo ========================================
echo  Starting FastAPI server...
echo ========================================
echo.
echo Server will be available at:
echo   http://localhost:5000
echo.
echo API Documentation:
echo   http://localhost:5000/docs
echo.
echo Health Check:
echo   http://localhost:5000/health
echo.
echo Press CTRL+C to stop the server
echo ========================================
echo.
python api.py

