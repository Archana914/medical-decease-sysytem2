# inspect_joblib.py
import joblib, pprint

for name in ("disease_model.joblib", "vectorizer.joblib"):
    try:
        obj = joblib.load(name)
    except Exception as e:
        print(f"FAILED to load {name}: {e}")
        continue
    print("="*60)
    print(name)
    print("type(obj):", type(obj))
    # If it's a class, printing _name_ will show class name
    try:
        print("obj.__class__.__name__:", obj.__class__.__name__)
    except Exception:
        pass
    # Print common attrs so we can tell if it's a trained estimator or a class
    attrs = []
    for a in ("predict", "fit", "vocabulary_", "get_feature_names_out"):
        attrs.append((a, hasattr(obj, a)))
    pprint.pprint(attrs)
    # If it's small, print repr
    try:
        r = repr(obj)
        print("repr(obj)[:300]:", r[:300])
    except Exception:
        pass