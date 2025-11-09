# minimal_server.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Minimal server OK"

if __name__ == "__main__":
    print("Starting minimal server now")
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)