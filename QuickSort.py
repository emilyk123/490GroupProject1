# Quick Sort Implementation
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Generate random numbers
random_list = [random.randint(10, 9999) for _ in range(10)]

print("Original Array: ", random_list)
sorted_arr = quick_sort(random_list)
print("Sorted Array: ", sorted_arr)