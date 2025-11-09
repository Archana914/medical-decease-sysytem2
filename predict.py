import joblib

model = joblib.load("disease_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

symptoms = input("Enter symptoms: ")  # e.g., fever cough
features = vectorizer.transform([symptoms])
prediction = model.predict(features)
print("Predicted Disease:", prediction[0])