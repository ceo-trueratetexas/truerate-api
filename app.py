
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Load environment variables
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
COLLECTIONS = os.getenv("COLLECTIONS", "").split(",")

# Load model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, token=HF_TOKEN, device_map="auto")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided."}), 400

    formatted_prompt = f"<s>[INST] {prompt.strip()} [/INST]"
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, temperature=0.7, top_p=0.9, top_k=50, repetition_penalty=1.2)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    to_email = data.get("to")
    subject = data.get("subject", "Message from TrueRate Texas")
    body = data.get("body", "This is a test email from TrueRate.")

    if not to_email:
        return jsonify({"error": "Recipient email required"}), 400

    response = requests.post(
        MAILGUN_DOMAIN,
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"TrueRate Texas <mailgun@{MAILGUN_DOMAIN.split('/')[3]}>",
            "to": [to_email],
            "subject": subject,
            "text": body
        }
    )

    if response.status_code == 200:
        return jsonify({"message": "✅ Email sent successfully"})
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
