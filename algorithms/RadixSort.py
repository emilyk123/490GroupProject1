def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n # store sorted values based on the current digit
    count = [0] * 10 # store the count of each digit

    # Count occurrences of each digit at the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

     # Update count[i] to store the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the output array by placing elements in the correct order
    # Start from the last element to maintain stable sorting
    for i in range(n-1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        yield arr

    # Copy the output array to arr[]
    for i in range(n):
        arr[i] = output[i]
        yield arr

def radix_sort(arr):
    max_num = max(arr) # Find the maximum number to determine the number of digits
    exp = 1 # Start with the least significant digit

    # Process each digit place until we process the largest number
    while max_num // exp > 0:
        yield from counting_sort(arr, exp)
        exp *= 10 # Move to the next digit place