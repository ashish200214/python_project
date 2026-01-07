from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "🚀 REST API is running"
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "python-rest-api",
        "status": "UP"
    })

@app.route("/user/<name>", methods=["GET"])
def user(name):
    return jsonify({
        "username": name,
        "role": "tester"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
