from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

with open("responses.txt", "r", encoding="utf-8") as file:
    responses = [line.strip() for line in file if line.strip()]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    return jsonify({"response": random.choice(responses)})

if __name__ == "__main__":
    app.run(debug=True)
