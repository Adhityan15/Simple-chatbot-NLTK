from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response
# given modules used herre

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_message = request.json["message"]
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
# python code for app interface for chatbot