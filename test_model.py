# test_model.py
import os, traceback, joblib

for p in ("disease_model.joblib","vectorizer.joblib"):
    print("-----", p, "-----")
    if not os.path.isfile(p):
        print("MISSING:", p)
        continue
    try:
        obj = joblib.load(p)
        print("LOADED:", p, "type:", type(obj))
        if hasattr(obj, "classes_"):
            print(" classes_ (sample):", getattr(obj, "classes_")[:10])
        if hasattr(obj, "vocabulary_"):
            print(" vocab size:", len(getattr(obj, "vocabulary_", {})))
    except Exception as e:
        print("ERROR loading", p, ":", e)
        traceback.print_exc()