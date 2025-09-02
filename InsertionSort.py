import random
"""Used for generating random test arrays to test mergesort"""

import statistics
"""Used for calculating mean, median, and standard deviation of the timing results"""

import time 
"""Used for Timing the algorithm execution time"""

def insertionsort(arr):
    """
    InsertionSort algorithm implementation.
    
    Args:
        arr (list): The array to be sorted

    Returns:
        list: Sorted array
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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

InsertionSort Algorithm Timing Tests

"""

sizes = [100, 500, 1000, 5000, 10000]
trials = 5

for n in sizes:
    times = []
    for trial in range(trials):
        test_array = list(range(1, n + 1))
        # random.seed(trial)
        random.shuffle(test_array)

        elapsed = time_algorithm(insertionsort, test_array)
        times.append(elapsed)

        if insertionsort(test_array) == sorted(test_array):
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


