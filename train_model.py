import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load data
df = pd.read_csv("dataset.csv")

# Convert text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["symptoms"])
y = df["disease"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
joblib.dump(model, "disease_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("Model trained and saved successfully!")