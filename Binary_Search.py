import time
import matplotlib.pyplot as plt

def Recursive_Binary_Search(A, x, low, high):
    if low > high:
        return -1  # Element not found
    
    mid = (low + high) // 2

    if A[mid] == x:
        return mid
    elif A[mid] < x:
        return Recursive_Binary_Search(A, x, mid + 1, high)
    else:
        return Recursive_Binary_Search(A, x, low, mid - 1)

# Function to measure the runtime of the binary search
def measure_runtime():
    sizes = []  # List to store input array sizes
    runtimes = []  # List to store corresponding runtimes

    for size in range(1, 10001, 100):  # Vary the input size from 1 to 10,000
        input_array = list(range(1, size + 1))  # Generate a sorted input array

        start_time = time.time()  # Record the start time
        target_index = Recursive_Binary_Search(input_array, size // 2, 0, size - 1)
        end_time = time.time()  # Record the end time

        elapsed_time = end_time - start_time  # Calculate the elapsed time
        sizes.append(size)
        runtimes.append(elapsed_time)

    return sizes, runtimes

# Measure runtime and create a plot
sizes, runtimes = measure_runtime()
plt.plot(sizes, runtimes)
plt.xlabel("Input Array Size")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime Analysis of Recursive Binary Search")
plt.grid()
plt.show()
