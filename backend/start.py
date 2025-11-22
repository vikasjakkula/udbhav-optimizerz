#!/usr/bin/env python
"""
Startup script for the Flask backend server
"""
import subprocess
import sys
import os

# Change to backend directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run the Flask app
if __name__ == '__main__':
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

