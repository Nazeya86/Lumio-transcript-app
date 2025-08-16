import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}
data = {"inputs": "Summarize this text: Artificial intelligence is changing the world rapidly."}

response = requests.post(MODEL_URL, headers=headers, json=data)
print(response.status_code)
print(response.json())
