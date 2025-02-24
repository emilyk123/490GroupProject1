# Define Function to perform linear search
def linear_search(L, T):
    result_array = []
    for index in range(len(L)):
        if L[index] == T:
            result_array.append(index)
    if len(result_array) == 0:
        return -1
    else:
        return result_array

# Take user input for list elements
user_input = input("Enter list elements separated by spaces: ")
L = list(map(int, user_input.split()))

# Take user input for the target element
T = int(input("Enter the target element to search: "))

# Calling the linear_search function
result = linear_search(L, T)

# Display the result
if result != -1:
    print(f"Element {T} found at indexes {result}")
else:
    print(f"Element {T} not found in the list")