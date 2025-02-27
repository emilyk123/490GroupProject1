def linear_search(arr, target):
    for i, num in enumerate(arr):
        yield (i, False, arr.copy())
        if num == target:
            yield (i, True, arr.copy())
            return
    yield (-1, False, arr.copy())