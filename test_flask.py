from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Flask is working!"

if __name__ == "_main_":
    app.run(host="127.0.0.1", port=5000)