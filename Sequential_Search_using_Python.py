def sequential_search(arr, target):
    """
    Perform a sequential search for the target in the array.

    Parameters:
    arr (list): The list to search through.
    target (any): The element to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Example usage:
arr = [5, 3, 7, 1, 9, 4]
target = 7
result = sequential_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")

