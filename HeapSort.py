import random
"""Used for generating random test arrays to test mergesort"""

import statistics
"""Used for calculating mean, median, and standard deviation of the timing results"""

import time 
"""Used for Timing the algorithm execution time"""

def heapify(arr, n, i):
    """
    Helper function to maintain the heap property.
    
    Args:
        arr (list): The array representing the heap
        n (int): Size of heap
        i (int): Index to heapify from
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Heapify the root

def heapsort(arr):
    """
    HeapSort algorithm implementation.
    
    Args:
        arr (list): The array to be sorted

    Returns:
        list: Sorted array
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)

    return arr


def time_algorithm(algo, arr):
    """
    Times the execution of the given algorithm on the provided array.

    Args:
        algo (function): The sorting algorithm to be timed
        arr (list): The array to be sorted
    
    Returns:
        float: Time taken to execute the algorithm in seconds
    """
    start = time.perf_counter()
    algo(arr.copy())
    return time.perf_counter() - start

"""

HeapSort Algorithm Timing Tests

"""

sizes = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
trials = 5

for n in sizes:
    times = []
    for trial in range(trials):
        test_array = list(range(1, n + 1))
        # random.seed(trial)
        random.shuffle(test_array)

        elapsed = time_algorithm(heapsort, test_array)
        times.append(elapsed)

        if heapsort(test_array) == sorted(test_array):
            print(f"Trial {trial+1} | n={n:<5} → {elapsed:.5f} seconds (Correctly sorted)")
        else:
            print(f"Trial {trial+1} | n={n:<5} → Sorting failed")

    mean_time = statistics.mean(times)
    median_time = statistics.median(times)
    stdev_time = statistics.stdev(times)

    print(f"→ Results for n={n:<5}: "
          f"Median={median_time:.5f}, "
          f"Mean={mean_time:.5f}, "
          f"StdDev={stdev_time:.5f}\n")