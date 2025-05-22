# This function performs binary search on a sorted list
def binary_search(arr, target):
    low = 0                   # Starting index
    high = len(arr) - 1       # Ending index

    # Repeat until the search space is empty
    while low <= high:
        mid = (low + high) // 2   # Find the middle index
        guess = arr[mid]          # Value at the middle index

        if guess == target:
            return mid            # Target found, return index
        elif guess < target:
            low = mid + 1         # Search in the right half
        else:
            high = mid - 1        # Search in the left half

    return -1  # Target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11, 13]
target_value = 7

result = binary_search(numbers, target_value)

if result != -1:
    print(f"Found at index: {result}")
else:
    print("Not found")
