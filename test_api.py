"""
Test script for Heart Attack Prediction API
"""
import requests
import json

# API base URL
BASE_URL = "http://localhost:5000"

def test_health():
    """Test health check endpoint"""
    print("=" * 60)
    print("Testing Health Check Endpoint")
    print("=" * 60)
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        print("✅ Health check passed!\n")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}\n")
        return False

def test_predict():
    """Test prediction endpoint with sample data"""
    print("=" * 60)
    print("Testing Prediction Endpoint")
    print("=" * 60)
    
    # Sample data matching frontend format
    sample_data = {
        "name": "John Doe",
        "age": 45,
        "sex": 1,  # 1 = Male, 0 = Female
        "cholesterol": 200,
        "bp": 120,  # Blood pressure
        "fbs": False,  # Fasting blood sugar > 120
        "thalachh": 150,  # Max heart rate achieved
        "diabetes": False,
        "obesity": False,
        "shortness_of_breath": False,
        "chest_pain": False,
        "sweating": False,
        "stress": False,
        "poor_sleep": False,
        "smoking": False
    }
    
    print(f"Request Data:")
    print(json.dumps(sample_data, indent=2))
    print("\nSending POST request to /predict...")
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ Prediction successful!")
            print(f"\nResponse:")
            print(json.dumps(result, indent=2))
            print(f"\n📊 Summary:")
            print(f"   - Probability: {result.get('probability', 0):.4f} ({result.get('probability', 0)*100:.2f}%)")
            print(f"   - Prediction: {result.get('prediction', 'N/A')}")
            print(f"   - Health Status: {result.get('health_status', 'N/A')}")
            print(f"   - Risk Percentage: {result.get('risk_percentage', 0)}%")
        else:
            print(f"❌ Prediction failed!")
            print(f"Response: {response.text}")
            
        return response.status_code == 200
        
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Server is not running!")
        print("   Please start the server first:")
        print("   python api.py")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_multiple_scenarios():
    """Test with multiple risk scenarios"""
    print("\n" + "=" * 60)
    print("Testing Multiple Scenarios")
    print("=" * 60)
    
    scenarios = [
        {
            "name": "Low Risk Scenario",
            "data": {
                "age": 30,
                "sex": 1,
                "cholesterol": 180,
                "bp": 110,
                "fbs": False,
                "thalachh": 180,
                "diabetes": False,
                "chest_pain": False,
                "shortness_of_breath": False,
                "smoking": False
            }
        },
        {
            "name": "High Risk Scenario",
            "data": {
                "age": 65,
                "sex": 1,
                "cholesterol": 280,
                "bp": 150,
                "fbs": True,
                "thalachh": 120,
                "diabetes": True,
                "chest_pain": True,
                "shortness_of_breath": True,
                "smoking": True
            }
        }
    ]
    
    for scenario in scenarios:
        print(f"\n📋 Testing: {scenario['name']}")
        try:
            response = requests.post(
                f"{BASE_URL}/predict",
                json=scenario['data'],
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                risk_percent = result.get('risk_percentage', 0)
                status = "🔴 HIGH RISK" if risk_percent > 50 else "🟡 MEDIUM RISK" if risk_percent > 30 else "🟢 LOW RISK"
                print(f"   {status} - {risk_percent}% probability")
            else:
                print(f"   ❌ Failed: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    print("\n🧪 Testing Heart Attack Prediction API")
    print("=" * 60)
    print(f"API URL: {BASE_URL}\n")
    
    # Test health check
    health_ok = test_health()
    
    if not health_ok:
        print("⚠️  Server is not running or health check failed.")
        print("   Please start the server with: python api.py")
        exit(1)
    
    # Test prediction
    print("\n")
    predict_ok = test_predict()
    
    # Test multiple scenarios
    if predict_ok:
        test_multiple_scenarios()
    
    print("\n" + "=" * 60)
    if health_ok and predict_ok:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
    print("=" * 60)

