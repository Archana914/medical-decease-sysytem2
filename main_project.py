import joblib, sqlite3
# Binary Search Function (DAA)
def binary_search(arr, target):
    arr = sorted(arr)  # ensure the list is sorted
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Related Diseases Function (BFS)
from collections import defaultdict, deque

def related_diseases(symptom):
    graph = defaultdict(list)
    graph["fever"].extend(["cold", "malaria"])
    graph["cough"].extend(["cold", "flu"])
    graph["headache"].extend(["flu", "migraine"])
    graph["nausea"].extend(["food poisoning", "malaria"])

    visited = set()
    q = deque([symptom])
    result = []

    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    result.append(neighbour)
                    q.append(neighbour)
    return result

# Load model
model = joblib.load("disease_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Take input
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

# DAA features
symptom_list = ["fever", "cough", "headache", "nausea"]
found = binary_search(symptom_list, "fever")
print("Is fever a known symptom?", found)

related = related_diseases("fever")
print("Diseases related to fever:", related)