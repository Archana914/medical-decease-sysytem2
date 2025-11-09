def binary_search(arr, target):
    arr.sort()
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

symptoms_list = ["fever","cough","headache","body pain","nausea"]
print(binary_search(symptoms_list, "fever"))  # True