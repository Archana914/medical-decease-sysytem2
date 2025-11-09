import joblib, sqlite3

model = joblib.load("disease_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

symptoms = input("Enter symptoms: ")
features = vectorizer.transform([symptoms])
prediction = model.predict(features)[0]
print("Predicted Disease:", prediction)

# Save to database
conn = sqlite3.connect('diagnosis.db')
cur = conn.cursor()
cur.execute("INSERT INTO predictions (symptoms, predicted_disease) VALUES (?, ?)", (symptoms, prediction))
conn.commit()
conn.close()
print("Prediction saved in database.")