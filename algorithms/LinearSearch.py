def linear_search(arr, target):
    for i, num in enumerate(arr):
        yield (i, False, arr.copy())
        # If the current number is equal to the target, return the index
        if num == target:
            yield (i, True, arr.copy())
            return
    yield (-1, False, arr.copy()) # If the target is not found, return