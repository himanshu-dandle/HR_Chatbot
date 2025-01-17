from flask import Flask, render_template, request, jsonify
from local_chatbot import get_chatbot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data.get("user_input", "")
    bot_response = get_chatbot_response(user_input)
       # Log interactions to a file
    with open("chat_logs.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\nBot: {bot_response}\n\n")
        
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=False)
