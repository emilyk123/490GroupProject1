def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        yield from merge_sort(left)
        yield from merge_sort(right)
        
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr
        
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