from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

df = pd.read_csv("dataset.csv")
vectorizer = joblib.load("vectorizer.joblib")
model = joblib.load("disease_model.joblib")

X = vectorizer.transform(df["symptoms"])
y = df["disease"]

y_pred = model.predict(X)

print("Accuracy:", accuracy_score(y, y_pred))
print("\nReport:\n", classification_report(y, y_pred))