'''
This script sorts the array using the Heap Sort Algorithm.

'''
def heapify (arr, n, i):
    largest = i  # Initialise 'largest' as the root index i
    left = 2 * i + 1  # Calculate the index of the left child of the node at index i
    right = 2 * i + 2 # Calculate the index of the right child of the node

    # Check if the left child exists and if it is greater than the root
    if left < n and arr[largest] < arr[left]:
        largest = left  # set largest to left

    # Check if the right child exists and if it is greater than current largest
    if right < n and arr[largest] < arr[right]:
        largest = right  # Set largest to right

    # If largest is not the root, swap the root with the largest chils
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # recursively heapify the subtree


def heap_sort(arr):
    # Get the length of the array
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # move the current root to end
        heapify(arr, i, 0) # heapify the reduced heap


if __name__ == "__main__":
    arr = [1, 12, 14, 3, 18, 4, 8]
    print("Original array:", arr)
    heap_sort(arr)
    print("Sorted array:", arr)