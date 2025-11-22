@echo off
echo Installing Python dependencies...
..\.venv\Scripts\python.exe -m pip install -r requirements.txt

echo.
echo Starting Flask server on http://localhost:5000
echo.
..\.venv\Scripts\python.exe app.py

