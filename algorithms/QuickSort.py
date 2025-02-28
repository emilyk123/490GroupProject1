def quick_sort(arr, low, high):
    if low < high: # If low >= high, the array is sorted
        pi = yield from partition(arr, low, high) # The partitioning index
        yield from quick_sort(arr, low, pi-1)
        yield from quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high] # Set pivot element
    i = low - 1 # Index of smaller element

    # If current element is smaller than the pivot
    # Swap the element at i+1 with the element at j
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield arr
    return i + 1