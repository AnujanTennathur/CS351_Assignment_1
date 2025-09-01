import random
"""Used for generating random test arrays to test mergesort"""

import statistics
"""Used for calculating mean, median, and standard deviation of the timing results"""

import time 
"""Used for Timing the algorithm execution time"""


"""

MergeSort Algorithm with Visualization and Timing

"""

def merge(left, right):
    """
    Merges the two sorted arrays
    
    Args: 
        left (list): Left sorted array
        right (list): Right sorted array

    Returns: 
        tuple: Merged sorted array and steps taken during merge

    """
    result = []
    i = j = 0
    
    steps = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            steps.append(f"Compare {left[i]} ≤ {right[j]}: Take {left[i]} from left")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"Compare {left[i]} > {right[j]}: Take {right[j]} from right")
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result, steps

def mergesort_visual(arr, depth=0):
    """
    The MergeSort algorithm with visualization steps to highlight the process.

    Args:
        arr (list): The array to be sorted
        depth (int): Current depth of recursion for indentation
    
    Returns:
        list: Sorted array
    
    """
    indent = "  " * depth
    print(f"{indent}Sorting: {arr}")
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = mergesort_visual(arr[:mid], depth + 1)
    right = mergesort_visual(arr[mid:], depth + 1)
    
    result, steps = merge(left, right)
    print(f"{indent}Merging {left} + {right} = {result}")
    
    return result


def mergesort(arr):
    """
    MergeSort without visualization steps. This is useful for timing the algorithm with large 
    input sizes because we do not want to include all of the print statements as this would 
    overrun the console and make it difficult to read.

    Args:
        arr (list): The array to be sorted

    Returns:
        list: Sorted array
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result, steps = merge(left, right)
    return result

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

Mergesort Tests

"""

sizes = [100, 500, 1000]
trials = 5

for n in sizes:
    times = []
    for trial in range(trials):
        test_array = list(range(1, n + 1))
        # random.seed(trial)
        random.shuffle(test_array)

        elapsed = time_algorithm(mergesort, test_array)
        times.append(elapsed)

        if mergesort(test_array) == sorted(test_array):
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













