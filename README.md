The Cardio Predictor – Heart Attack Early Warning System
Team ID: udbhav_015 (UDHBAV 2025)
🚨 Problem Statement

Heart attacks often strike without any visible early symptoms.
In many hospitals, doctors struggle to identify high-risk patients because:

Medical records are incomplete

Risk factors vary across patients

Traditional scoring methods are not accurate enough

As a result, many individuals receive help only after a major cardiac event occurs.

💡 Our Solution

The Cardio Predictor is an AI-based heart risk prediction tool that helps doctors identify at-risk patients years before symptoms occur.

The system:

Analyzes patient health data

Calculates a clear heart attack risk percentage

Works accurately even with missing / incomplete data

Highlights the top factors contributing to the risk (Explainable AI)

This improves decision-making and enables early prevention.

🧠 Key Features

Risk Scoring: Predicts heart attack probability

Missing Data Handling: Robust model using Random Forest

Explainability: Shows top risk factors

Doctor Dashboard: Simple UI for easy use

Trained on Real Dataset: UCI Heart Disease dataset

🔍 Why This Idea is Novel

Combines medical risk scoring + explainable ML

Works even with incomplete hospital data

Designed specifically to fit Indian clinical workflows

Fast, lightweight, deployable in rural clinics

Transparent outputs → doctors can trust predictions

🛠 Tech Stack

Machine Learning Models:

Random Forest

Logistic Regression

Dataset: UCI Heart Disease Dataset

Languages: Python

UI / Dashboard: (Your team's UI tech here)

Libraries: NumPy, pandas, scikit-learn, matplotlib, etc.

🔧 System Architecture
        +------------------------+
        |     Patient Input      |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |  Preprocessing Module  |
        | (handles missing data) |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |   ML Model (RF + LR)  |
        |  Predicts risk score  |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |   Explanation Engine   |
        | Shows top risk factors |
        +-----------+------------+
                    |
                    v
        +------------------------+
        |   Doctor Dashboard     |
        +------------------------+

📊 Sample Output Screenshot

(Add image or placeholder)

Risk Score: 72% (High Risk)
Top Factors:
- Cholesterol  
- Max heart rate  
- Chest pain type  

🧪 How to Run
pip install -r requirements.txt
python model.py
python app.py


(Modify based on your code.)

🚀 Future Scope

Integrate with smartwatches & BP monitors

Connect with hospital EMR systems

Add ECG and long-term trends for better accuracy

Build a patient mobile app for continuous monitoring

Deploy as offline-first for rural clinics

Add multilingual voice input for doctors

Provide weekly auto-checkups for high-risk patients

📅 Project Plan (Completeness of Plan — 20/20)
Day 1:

Dataset cleanup

Model selection

Baseline accuracy

Day 2:

Dashboard UI

Model integration

Input validations

Day 3:

Testing

Output visualization

Presentation + demo preparation

Future:

Full deployment version

Hospital trials

👥 Team Members

Harsha — Presentation Lead, Demo Flow

Vikas — Model Development

Suchay — Data Preprocessing

Adithya — Dashboard + Integration

⭐ Conclusion

The Cardio Predictor empowers hospitals to detect heart attack risk before it's too late, making early intervention possible and saving lives.