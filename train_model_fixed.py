# train_model_fixed.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import joblib

# Edit these if your CSV has different column names:
TEXT_COL = "text"     # or "symptoms"
LABEL_COL = "label"   # or "disease"

df = pd.read_csv("dataset.csv")

if TEXT_COL not in df.columns or LABEL_COL not in df.columns:
    print("CSV columns:", df.columns.tolist())
    raise SystemExit(f"Update TEXT_COL/LABEL_COL in train_model_fixed.py to match your CSV columns")

X = df[TEXT_COL].astype(str)
y = df[LABEL_COL].astype(str)

vectorizer = CountVectorizer()
Xv = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(Xv, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

joblib.dump(model, "disease_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("✅ Saved disease_model.joblib and vectorizer.joblib")