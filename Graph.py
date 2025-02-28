from MergeSortAlgorithm import merge_sort
import matplotlib.pyplot as plt
import time
from decimal import *
import random



class Graph:
    def __init__(self):
        self.runtimes = {
            'Bubble Sort': {5:0, 10:0, 20:0},
            'Merge Sort': {5:0, 10:0, 20:0},
            'Quick Sort': {5:0, 10:0, 20:0},
            'Radix Sort': {5:0, 10:0, 20:0},
            'Linear Search': {5:0, 10:0, 20:0}
        }
        file = open("sorting_times.txt", "r")
        for line in file:
            list = line.strip().split(',')
            list[1] = int(list[1])
            self.runtimes[list[0]][list[1]] = (list[2])
        print(self.runtimes['Bubble Sort'][5])

    # Create Bar Graph
    #algorithms = ['Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search']
    # Place holders for Bubble, quick, radix, and linear
    #runtimes = [merge_runtime, merge_runtime, merge_runtime, merge_runtime, merge_runtime]

    def create_graph(self):
        bar_graph = plt.subplot(111)
        array_sizes = [5, 10, 20]
        for i in range(3):
            bar_graph.bar(i + 1 - 0.2, float(self.runtimes['Bubble Sort'][array_sizes[i]]), width=0.1, color='b', align='center')
            bar_graph.bar(i + 1 - 0.1, float(self.runtimes['Merge Sort'][array_sizes[i]]), width=0.1, color='c', align='center')
            bar_graph.bar(i + 1, float(self.runtimes['Quick Sort'][array_sizes[i]]), width=0.1, color='g', align='center')
            bar_graph.bar(i + 1 + 0.1, float(self.runtimes['Radix Sort'][array_sizes[i]]), width=0.1, color='m', align='center')
            bar_graph.bar(i + 1 + 0.2, float(self.runtimes['Linear Search'][array_sizes[i]]), width=0.1, color='r', align='center')

        bar_graph.get_xaxis().set_ticks([])
        plt.title('Runtime Complexity Analysis')
        plt.xlabel('Input')
        plt.ylabel('Runtime in s')
        plt.draw()
