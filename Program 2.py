def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid  # Element found
        elif arr[mid] < key:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Element not found


# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
key = 7

result = binary_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")