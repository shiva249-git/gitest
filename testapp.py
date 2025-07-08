from flask import Flask, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Use environment variable for safety
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/")
def index():
    return "✅ Test App is Running"

@app.route("/test-api")
def test_api():
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": "Say hello in 5 words"}
            ]
        )
        return jsonify({
            "success": True,
            "reply": response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
