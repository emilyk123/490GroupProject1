def quick_sort(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high)
        yield from quick_sort(arr, low, pi-1)
        yield from quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr
    arr[i+1], arr[high] = arr[high], arr[i+1]
    yield arr
    return i + 1