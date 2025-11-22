# API Request Examples for Postman

## Predict API - POST Request

### Endpoint
```
POST http://localhost:5000/predict
```

### Headers
```
Content-Type: application/json
```

### cURL Command (Copy this to Postman)

#### Example 1: Low Risk Patient
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "age": 30,
    "sex": 1,
    "cholesterol": 180,
    "bp": 110,
    "fbs": false,
    "thalachh": 180,
    "diabetes": false,
    "obesity": false,
    "shortness_of_breath": false,
    "chest_pain": false,
    "sweating": false,
    "stress": false,
    "poor_sleep": false,
    "smoking": false
  }'
```

#### Example 2: High Risk Patient
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "age": 65,
    "sex": 1,
    "cholesterol": 280,
    "bp": 150,
    "fbs": true,
    "thalachh": 120,
    "diabetes": true,
    "obesity": true,
    "shortness_of_breath": true,
    "chest_pain": true,
    "sweating": true,
    "stress": true,
    "poor_sleep": true,
    "smoking": true
  }'
```

#### Example 3: Medium Risk Patient
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Mike Johnson",
    "age": 45,
    "sex": 1,
    "cholesterol": 200,
    "bp": 120,
    "fbs": false,
    "thalachh": 150,
    "diabetes": false,
    "obesity": false,
    "shortness_of_breath": false,
    "chest_pain": false,
    "sweating": false,
    "stress": false,
    "poor_sleep": false,
    "smoking": false
  }'
```

### JSON Body (Raw - For Postman)

**Low Risk Example:**
```json
{
  "name": "John Doe",
  "age": 30,
  "sex": 1,
  "cholesterol": 180,
  "bp": 110,
  "fbs": false,
  "thalachh": 180,
  "diabetes": false,
  "obesity": false,
  "shortness_of_breath": false,
  "chest_pain": false,
  "sweating": false,
  "stress": false,
  "poor_sleep": false,
  "smoking": false
}
```

**High Risk Example:**
```json
{
  "name": "Jane Smith",
  "age": 65,
  "sex": 1,
  "cholesterol": 280,
  "bp": 150,
  "fbs": true,
  "thalachh": 120,
  "diabetes": true,
  "obesity": true,
  "shortness_of_breath": true,
  "chest_pain": true,
  "sweating": true,
  "stress": true,
  "poor_sleep": true,
  "smoking": true
}
```

### Expected Response Format

```json
{
  "probability": 0.8929,
  "prediction": 1,
  "risk_percentage": 89.29,
  "health_status": "High Risk"
}
```

## Field Descriptions

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `name` | string | Patient name (optional) | No |
| `age` | number | Patient age in years | Yes |
| `sex` | integer | 1 = Male, 0 = Female | Yes |
| `cholesterol` | number | Cholesterol in mg/dL | Yes |
| `bp` | number | Blood pressure in mmHg | Yes |
| `fbs` | boolean | Fasting blood sugar > 120 mg/dl | No |
| `thalachh` | number | Maximum heart rate achieved | No |
| `diabetes` | boolean | Diabetes status | No |
| `obesity` | boolean | Obesity status | No |
| `shortness_of_breath` | boolean | Shortness of breath | No |
| `chest_pain` | boolean | Chest pain | No |
| `sweating` | boolean | Sweating | No |
| `stress` | boolean | Stress | No |
| `poor_sleep` | boolean | Poor sleep | No |
| `smoking` | boolean | Smoking status | No |

## How to Use in Postman

1. **Open Postman**
2. **Create a new request**
3. **Set method to:** `POST`
4. **Enter URL:** `http://localhost:5000/predict`
5. **Go to Headers tab** and add:
   - Key: `Content-Type`
   - Value: `application/json`
6. **Go to Body tab**
   - Select `raw`
   - Select `JSON` from dropdown
   - Paste one of the JSON examples above
7. **Click Send**

## Health Check Endpoint

**GET Request:**
```
GET http://localhost:5000/health
```

**cURL:**
```bash
curl -X GET http://localhost:5000/health
```

## API Documentation

Once the server is running, you can access interactive API docs at:
```
http://localhost:5000/docs
```

