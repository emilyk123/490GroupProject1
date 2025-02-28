def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False # Flag to check if any swap happened in this pass
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]: # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr
        # If no two elements were swapped in the inner loop, then
        if not swapped: 
            break
        yield arr # Return the array after each pass