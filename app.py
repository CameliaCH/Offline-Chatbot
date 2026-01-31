from flask import Flask, request, jsonify

app = Flask(__name__)

def handle_message(msg):
    return f"u said {msg}"

@app.route("/chat",methods = ["POST"])
def chat():
    msg = request.json["message"]
    reply = handle_message(msg)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=5001)

#flask --app app run --debug