
from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize Flask
app = Flask(__name__)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"error": "No prompt provided."}), 400

        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-4-turbo" if available for faster response
            messages=[
                {"role": "system", "content": "You are Tex, a helpful assistant trained to generate structured and persuasive documentation for property tax protests in Texas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        result = response.choices[0].message['content']
        return jsonify({"response": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
