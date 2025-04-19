import requests

test_emails = [
    "Your account has been compromised. Click here to reset your password.",  # phishing
    "Please update your payment method to avoid cancellation.",               # phishing
    "Let’s meet next week to finalize the presentation.",                     # legit
    "Reminder: Your doctor’s appointment is scheduled for tomorrow.",        # legit
    "Urgent: Verify your identity now to avoid account lockout!",            # phishing
]

print("🔍 Running phishing detection tests...\n")

for email in test_emails:
    response = requests.post("http://localhost:5001/predict", json={"emailText": email})
    if response.ok:
        result = response.json()
        print(f"📩 Email: {email}")
        print(f"🔒 Prediction: {result['prediction']} | Confidence: {result['confidence']}\n")
    else:
        print("❌ Error:", response.text)


