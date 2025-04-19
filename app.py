from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Setup Flask app
app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}}, supports_credentials=True)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("📨 Received data:", data)

    if not data or 'emailText' not in data:
        return jsonify({'error': 'Missing emailText'}), 400

    email_text = data['emailText']
    email_vec = vectorizer.transform([email_text])
    prediction = model.predict(email_vec)[0]

    # Get phishing confidence specifically (assuming 'phishing' is label 1)
    proba = model.predict_proba(email_vec)[0]

    # Find the index of the 'phishing' class
    phishing_index = list(model.classes_).index('phishing')

    # Get phishing confidence score
    phishing_confidence = round(proba[phishing_index] * 100, 2)

    return jsonify({
        'prediction': prediction,
        'confidence': phishing_confidence,
        'advice': 'Avoid clicking on suspicious links or giving personal info.' if prediction == 'phishing' else 'Looks safe, but stay cautious.'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
