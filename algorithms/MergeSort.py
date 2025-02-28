def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Finding the middle of the array
        left = arr[:mid] # Dividing the array elements into 2 halves
        right = arr[mid:]
        yield from merge_sort(left) # Sorting the first half
        yield from merge_sort(right) # Sorting the second half
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            # Comparing elements from both halves 
            # Then add the smallest element to the sorted list
            if left[i] < right[j]: 
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr
        
        # Checking if any element was left
        # If yes, add it to the sorted list
        while i < len(left):
            arr[k] = left[i] 
            i += 1
            k += 1
            yield arr
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr