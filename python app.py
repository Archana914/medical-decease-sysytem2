from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Simple home route so you can check server in browser
@app.route("/")
def home():
    return "✅ Flask server is running!"

# Simple predict route (adjust for your model files)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True) or {}
    symptoms = data.get("symptoms", "")
    # If model/vectorizer missing, return friendly message
    model_path = "disease_model.joblib"
    vectorizer_path = "vectorizer.joblib"
    if not os.path.isfile(model_path) or not os.path.isfile(vectorizer_path):
        return jsonify({"error": "Model or vectorizer file missing. Run training first."}), 500

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    features = vectorizer.transform([symptoms])
    prediction = model.predict(features)[0]
    return jsonify({"predicted_disease": str(prediction)})

if __name__ == "__main__":
    # Use 0.0.0.0 if you need access from other machines; 127.0.0.1 is local only.
    app.run(host="127.0.0.1", port=5000, debug=True)
     