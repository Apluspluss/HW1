import timeit
import matplotlib.pyplot as plt

def Recursive_Binary_Search(A, x, low, high):
    if low > high:
        return -1  # Element not found
    
    mid = (low + high) // 2
    

     # Element found at index mid
    if A[mid] == x:
        return mid
    # Search in the right half
    elif A[mid] < x:
        return Recursive_Binary_Search(A, x, mid + 1, high)
    # Search in the left half
    else:
        return Recursive_Binary_Search(A, x, low, mid - 1)

def measure_runtime(n, num_runs=100000):
    # Create a sorted list of size n
    my_list = list(range(n))
    
    # Perform binary search on a target element not in the list
    target = -1
    
    # Measure runtime using timeit
    runtime = timeit.timeit(lambda: Recursive_Binary_Search(my_list, target, 0, n - 1), number=num_runs)
    
    # Calculate average runtime
    average_runtime = runtime / num_runs
    
    return average_runtime

# Test different input sizes and measure runtimes
input_sizes = [10, 10000, 40000, 60000, 80000, 100000]
runtimes = []

for size in input_sizes:
    runtime = measure_runtime(size)
    runtimes.append(runtime)

# Create a plot
plt.plot(input_sizes, runtimes, marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Average Runtime (seconds)')
plt.title('Binary Search Runtime vs Input Size')
plt.grid(True)

# Show the plot
plt.show()
