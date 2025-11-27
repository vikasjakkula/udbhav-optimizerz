# PowerShell script to test the Predict API

# Example 1: Low Risk Patient
Write-Host "Testing Low Risk Patient..." -ForegroundColor Green
$body = @{
    name = "John Doe"
    age = 30
    sex = 1
    cholesterol = 180
    bp = 110
    fbs = $false
    thalachh = 180
    diabetes = $false
    obesity = $false
    shortness_of_breath = $false
    chest_pain = $false
    sweating = $false
    stress = $false
    poor_sleep = $false
    smoking = $false
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://localhost:5000/predict" -Method POST -ContentType "application/json" -Body $body
Write-Host "Response:" -ForegroundColor Cyan
$response | ConvertTo-Json -Depth 10

Write-Host "`n" -NoNewline

# Example 2: High Risk Patient
Write-Host "Testing High Risk Patient..." -ForegroundColor Yellow
$body2 = @{
    name = "Jane Smith"
    age = 65
    sex = 1
    cholesterol = 280
    bp = 150
    fbs = $true
    thalachh = 120
    diabetes = $true
    obesity = $true
    shortness_of_breath = $true
    chest_pain = $true
    sweating = $true
    stress = $true
    poor_sleep = $true
    smoking = $true
} | ConvertTo-Json

$response2 = Invoke-RestMethod -Uri "http://localhost:5000/predict" -Method POST -ContentType "application/json" -Body $body2
Write-Host "Response:" -ForegroundColor Cyan
$response2 | ConvertTo-Json -Depth 10

