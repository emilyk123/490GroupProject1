def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        yield arr

    for i in range(n):
        arr[i] = output[i]
        yield arr

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        yield from counting_sort(arr, exp)
        exp *= 10