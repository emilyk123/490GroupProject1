"""
Sorting Algorithm Visualizer:   
    A tool that demonstrates various sorting algorithms
    with real-time visualization using matplotlib.

Course: CPSC 335-12
Group 12: Shuo Wang, Emily Krohn, Quan Khong
Date: 2025-02-26
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, RadioButtons
import time
import random
from algorithms.BubbleSort import bubble_sort
from algorithms.MergeSort import merge_sort
from algorithms.QuickSort import quick_sort
from algorithms.RadixSort import radix_sort
from algorithms.LinearSearch import linear_search

class SortingVisualizer:
    """Main visualization class handling UI and algorithm execution."""
    
    def __init__(self):
        """Initialize visualization components and UI elements."""
        # Setup figure and axes
        self.fig, self.ax = plt.subplots(figsize=(12, 7))
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.25)
        
        # Algorithm control variables
        self.original_arr = []       # The stored unsorted array for performance comparison
        self.arr = []                # Working array for visualization
        self.generator = None        # Generator for algorithm steps
        self.sorting = False         # Execution status flag
        self.paused = False          # Pause state flag
        self.start_time = 0          # Performance timer
        self.current_algo = "Bubble Sort"  # Default selected algorithm
        self.target = None           # Target for Linear Search

        # Generating a random array, size based on user's selection
        self.array_size_options = [5, 10, 20]
        self.current_array_size_index = 0
        self.current_array_size = self.array_size_options[self.current_array_size_index]
        
        # Initialize UI components
        self._create_controls()
        
        # Initial plot setup
        self.bars = self.ax.bar([], [])
        self.ax.set_title("Algorithm Visualizer", fontsize=16)

    def _create_controls(self):
        """Create and arrange all UI control elements."""
        # Algorithm selection using RadioButtons
        algo_ax = plt.axes([0.05, 0.65, 0.15, 0.3], facecolor='lightgoldenrodyellow')
        self.algo_radio = RadioButtons(
            algo_ax, 
            ('Bubble Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort', 'Linear Search')
        )
        self.algo_radio.on_clicked(self._set_algorithm)
        
        # Array input textbox for custom array input
        # Increased width to display the full generated array
        array_ax = plt.axes([0.25, 0.15, 0.5, 0.06])
        self.array_input = TextBox(array_ax, 'Array (Separate by Comma): ')
        self.array_input.on_submit(self._set_array)
        
        # Target input textbox for Linear Search algorithm
        target_ax = plt.axes([0.25, 0.08, 0.15, 0.06])
        self.target_input = TextBox(target_ax, 'Target (for Linear Search): ')
        self.target_input.on_submit(self._set_target)
        
        # Simulated dropdown button for selecting array size
        # Placed to the left of the "Random Array" button
        dropdown_ax = plt.axes([0.77, 0.15, 0.1, 0.06])
        self.size_dropdown = Button(dropdown_ax, f"Size: {self.current_array_size}")
        self.size_dropdown.on_clicked(self._cycle_array_size)
        
        # Button to generate a random array
        random_ax = plt.axes([0.88, 0.15, 0.07, 0.06])
        self.random_btn = Button(random_ax, 'Random Array')
        self.random_btn.on_clicked(self._generate_random)
        
        # Control buttons: Start, Pause, Reset
        start_ax = plt.axes([0.25, 0.01, 0.1, 0.06])
        self.start_btn = Button(start_ax, 'Start')
        self.start_btn.on_clicked(self._start_algorithm)
        
        pause_ax = plt.axes([0.37, 0.01, 0.1, 0.06])
        self.pause_btn = Button(pause_ax, 'Pause')
        self.pause_btn.on_clicked(self._toggle_pause)
        
        reset_ax = plt.axes([0.49, 0.01, 0.1, 0.06])
        self.reset_btn = Button(reset_ax, 'Reset')
        self.reset_btn.on_clicked(self._reset)

    def _cycle_array_size(self, _event):
        """
        Simulate a dropdown for array size selection.
        Cycles through the available options and updates the button label.
        """
        self.current_array_size_index = (self.current_array_size_index + 1) % len(self.array_size_options)
        self.current_array_size = self.array_size_options[self.current_array_size_index]
        self.size_dropdown.label.set_text(f"Size: {self.current_array_size}")
        self.fig.canvas.draw_idle()
        print(f"Selected array size: {self.current_array_size}")

    def _set_algorithm(self, label):
        """
        Callback to set the current algorithm based on RadioButtons selection.
        Also resets the working array to the stored original unsorted array.
        """
        self.current_algo = label
        print(f"Algorithm selected: {self.current_algo}")
        if self.original_arr and not self.sorting:
            self.arr = self.original_arr.copy()
            self._update_plot()

    def _set_array(self, text):
        """
        Parse and set the array from the provided comma-separated input.
        Also store it as the fixed original array for subsequent runs.
        """
        try:
            self.original_arr = [int(item.strip()) for item in text.split(',') if item.strip()]
            self.arr = self.original_arr.copy()
            self._update_plot()
        except ValueError: 
            print("Invalid array input. Please enter comma-separated integers.")

    def _set_target(self, text):
        """Set the target value for Linear Search."""
        try:
            self.target = int(text.strip())
        except ValueError:
            self.target = text.strip()

    def _generate_random(self, _event):
        """
        Generate a random array of integers using the selected array size, 
        store it as the original and update the plot.
        """
        size = self.current_array_size
        self.original_arr = [random.randint(1, 100) for _ in range(size)]
        self.arr = self.original_arr.copy()
        # Update the text box to display the full array
        self.array_input.set_val(', '.join(map(str, self.arr)))
        self._update_plot()
        print(f"New random array generated of size {size}: {self.arr}")

    def _start_algorithm(self, _event):
        """
        Initialize and start the selected algorithm using the fixed original array.
        This ensures each algorithm runs on the same unsorted input.
        """
        if not self.sorting and self.original_arr:
            self.sorting = True
            self.start_time = time.time()
            
            # Map algorithms to their generators, using a copy of the original unsorted array
            algo_map = {
                'Bubble Sort': lambda: bubble_sort(self.original_arr.copy()),
                'Merge Sort': lambda: merge_sort(self.original_arr.copy()),
                'Quick Sort': lambda: quick_sort(self.original_arr.copy(), 0, len(self.original_arr)-1),
                'Radix Sort': lambda: radix_sort(self.original_arr.copy()),
                'Linear Search': lambda: linear_search(self.original_arr.copy(), self.target)
            }
            
            self.generator = algo_map[self.current_algo]()
            self._next_step()

    def _next_step(self):
        """Execute the next step of the algorithm visualization."""
        if self.paused or not self.sorting:
            return
            
        try:
            if self.current_algo == 'Linear Search':
                # Linear search yields the next index to check
                step = next(self.generator)
                idx, found, _ = step
                self._update_plot(highlight_idx=idx, found=found)
                if found:
                    self.sorting = False
                    self._log_time()
            else:
                # Sorting algorithms yield new array states
                new_arr = next(self.generator)
                self.arr = new_arr
                self._update_plot()
            
            plt.pause(0.05)
            self._next_step()
        except StopIteration:
            self.sorting = False
            if self.current_algo != 'Linear Search':
                self._log_time()

    def _update_plot(self, highlight_idx=-1, found=False):
        """
        Update the bar plot visualization.
        Red for the current index (or green if found).

        Update the x-axis shows indices from 1 to the number of elements.
        Update the y-axis is fixed to 10, 20, …, 100.
        """
        self.ax.clear()
        n = len(self.arr)
        colors = ['skyblue'] * n

        if 0 <= highlight_idx < n:
            colors[highlight_idx] = 'red' if not found else 'green'

        self.bars = self.ax.bar(range(n), self.arr, color=colors)

        # Set x-axis tick positions and labels from 1 to n
        if n > 0:
            self.ax.set_xticks(range(n))
            xlabels = [str(i + 1) for i in range(n)]
            self.ax.set_xticklabels(xlabels)

        # Set y-axis: fixed ticks of 10,20,...,100
        if self.arr:
            self.ax.set_ylim(0, 100)
            yticks = list(range(10, 101, 10))
            self.ax.set_yticks(yticks)

        self.ax.set_xlabel("Array Index")
        self.ax.set_ylabel("Array Value")
        self.ax.set_title(f"{self.current_algo} Visualization", fontsize=16)
        plt.draw()

    def _toggle_pause(self, _event):
        """
        Toggle between pausing and resuming the algorithm visualization.
        Also update the pause button label accordingly.
        """
        self.paused = not self.paused
        if self.paused:
            self.pause_btn.label.set_text("Resume")
            print("Paused")
        else:
            self.pause_btn.label.set_text("Pause")
            self._next_step()
            print("Resumed")
        self.fig.canvas.draw_idle()

    def _reset(self, _event):
        """Reset the visualization and control variables."""
        self.sorting = False
        self.paused = False
        self.generator = None
        self.arr = []
        self.original_arr = []
        self.array_input.set_val("")
        self.target_input.set_val("")
        self.ax.clear()
        self.ax.set_title("Algorithm Visualizer", fontsize=16)
        plt.draw()

    def _log_time(self):
        """Record the algorithm execution time to a file."""
        elapsed = time.time() - self.start_time
        with open('sorting_times.txt', 'a') as f:
            f.write(f"{self.current_algo}, Array Size: {len(self.original_arr)}, Time: {elapsed:.6f}s\n")
        print(f"{self.current_algo} completed in {elapsed:.2f}s")

if __name__ == '__main__':
    visualizer = SortingVisualizer()
    plt.show()
