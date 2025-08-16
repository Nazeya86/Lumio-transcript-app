from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import requests  # Add this at the top of your Python file



# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

# Hugging Face API
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"  # example summarization model
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Email credentials
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Serve frontend
@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

# Generate AI summary using Hugging Face
@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    data = request.json
    transcript = data.get('transcript')

    if not transcript:
        return jsonify({'error': 'Transcript required'}), 400

    try:
        payload = {"inputs": transcript}
        response = requests.post(HF_MODEL_URL, headers=headers, json=payload)
        result = response.json()

        print("HF API response:", result)  # Debug: see full response

        # Extract summary
        if isinstance(result, list) and "summary_text" in result[0]:
            summary = result[0]['summary_text']
        elif isinstance(result, dict) and "error" in result:
            return jsonify({'error': result['error']}), 500
        else:
            summary = "No summary generated. Check your input or model."

        return jsonify({'summary': summary})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

# Send summary via email
@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    recipients = data.get('recipients')
    summary = data.get('summary')

    if not recipients or not summary:
        return jsonify({'error': 'Recipients and summary required'}), 400

    try:
        msg = EmailMessage()
        msg['Subject'] = 'Meeting Summary'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipients
        msg.set_content(summary)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({'message': 'Email sent successfully!'})

    except Exception as e:
        print("Email Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
