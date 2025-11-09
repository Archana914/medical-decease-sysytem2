from collections import defaultdict, deque

# Step 1: Create a disease-symptom graph
graph = defaultdict(list)
graph["fever"].extend(["cold", "malaria"])
graph["cough"].extend(["cold", "flu"])
graph["headache"].extend(["flu", "migraine"])
graph["nausea"].extend(["food poisoning", "malaria"])

# Step 2: BFS to find related diseases
def related_diseases(symptom):
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

# Example test
print("Related diseases for fever:", related_diseases("fever"))