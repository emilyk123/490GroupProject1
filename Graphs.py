from MergeSortAlgorithm import merge_sort
import matplotlib.pyplot as plt
import time
from decimal import *
import random

# Take user input
number_flights = int(input("Enter number of flights: "))
flights = []
for _ in range(number_flights):
    flight_no = 3 #input("Enter flight number: ")
    dep_time = random.randint(10, 9999) #int(input(f"Enter departure time for {flight_no}: "))
    flights.append((flight_no, dep_time))

# Measure the execution time
start_time = time.time()
merge_sort(flights)
end_time = time.time()
getcontext().prec = 25
merge_runtime = (Decimal(end_time) - Decimal(start_time)) * 1000000000


# Create Bar Graph
#algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search']
# Place holders for Bubble, quick, radix, and linear
#runtimes = [merge_runtime, merge_runtime, merge_runtime, merge_runtime, merge_runtime]

num_arrays = 4

bar_graph = plt.subplot(111)
for i in range(num_arrays):
    bar_graph.bar(i + 1 - 0.2, merge_runtime, width=0.2, color='b', align='center')
    bar_graph.bar(i + 1, merge_runtime, width=0.2, color='g', align='center')
    bar_graph.bar(i + 1 + 0.2, merge_runtime, width=0.2, color='r', align='center')

bar_graph.get_xaxis().set_ticks([])
plt.title('Runtime Complexity Analysis')
plt.xlabel('Input')
plt.ylabel('Runtime in ns')
plt.show()