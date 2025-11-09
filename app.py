from flask import Flask, request, jsonify, render_template
import joblib
import os

# Paths (adjust if your joblib files are elsewhere)
MODEL_FILE = "disease_model.joblib"
VECT_FILE = "vectorizer.joblib"

# load model + vectorizer (fall back with clear error)
def load_objects():
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(f"{MODEL_FILE} not found in working dir.")
    if not os.path.exists(VECT_FILE):
        raise FileNotFoundError(f"{VECT_FILE} not found in working dir.")
    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECT_FILE)
    return model, vectorizer

model, vectorizer = load_objects()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # renders templates/index.html
    return render_template("index.html")

@app.route("/predict", methods=["POST"]) 
def predict():
    try:
        # get data from form or json
        symptoms = request.form.get("symptoms") or (request.json and request.json.get("symptoms"))
        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400

        X = vectorizer.transform([symptoms])
        pred = model.predict(X)[0]

        # if AJAX JSON request - return JSON, otherwise render page with result
        if request.is_json or request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"prediction": str(pred)})
        else:
            return render_template("index.html", prediction=str(pred), symptoms=symptoms)
    except Exception as e:
        # return error info for debugging (don't expose in production)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Flask app (http://127.0.0.1:5000)...")
    app.run(host="127.0.0.1", port=5000, debug=True)