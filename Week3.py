import math
import time
import random
import logging

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Set the logging level to debug

# Create file handler which logs even debug messages
fh = logging.FileHandler('test_output.log', mode='w')
fh.setLevel(logging.DEBUG)

# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)  # Set to INFO to display less verbose messages on console, change to DEBUG for more

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def FindMaxSubarrayBruteForce(A, low, high):
    max_sum = -math.inf
    left = right = 0
    for i in range(low, high):
        temp_sum = 0
        for j in range(i, high):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                left, right = i, j
    return (left, right, max_sum)

def FindMaxCrossingSubarray(A, low, mid, high):
    left_sum = -math.inf
    sum = 0
    left = mid
    for i in reversed(range(low, mid)):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            left = i

    right_sum = -math.inf
    sum = 0
    right = mid - 1
    for j in range(mid, high):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            right = j

    return (left, right, left_sum + right_sum)

def FindMaxSubarrayRecursive(A, low, high):
    if low + 1 == high:
        return (low, high - 1, A[low])

    mid = (low + high) // 2
    left = FindMaxSubarrayRecursive(A, low, mid)
    right = FindMaxSubarrayRecursive(A, mid, high)
    cross = FindMaxCrossingSubarray(A, low, mid, high)
    if left[2] >= right[2] and left[2] >= cross[2]:
        return left
    elif right[2] >= left[2] and right[2] >= cross[2]:
        return right
    else:
        return cross

total_crossover_points = 0
num_runs = 5

for run in range(num_runs):
    NUM_ITERATIONS = 1000
    logger.debug(f'Starting run {run+1} with NUM_ITERATIONS={NUM_ITERATIONS}')

    for input_size in range(2, 100):
        arr = [random.randint(-100, 100) for _ in range(input_size)]
        logger.debug(f'Testing input size {input_size}')

        # Measure Brute force method
        start = time.time()
        for _ in range(NUM_ITERATIONS):
            FindMaxSubarrayBruteForce(arr, 0, len(arr))
        bf_time = (time.time() - start) / NUM_ITERATIONS

        # Measure Recursive method
        start = time.time()
        for _ in range(NUM_ITERATIONS):
            FindMaxSubarrayRecursive(arr, 0, len(arr))
        rc_time = (time.time() - start) / NUM_ITERATIONS

        logger.debug(f'Input Size: {input_size}, BruteForce Time: {bf_time}, Recursive Time: {rc_time}')

        if bf_time > rc_time:
            logger.info(f"Run {run+1}: Crossover point found at input size = {input_size}")
            total_crossover_points += input_size
            break

if total_crossover_points > 0:
    average_crossover_point = total_crossover_points / num_runs
    logger.info(f"Average Crossover Point after {num_runs} runs: {average_crossover_point}")
else:
    logger.warning("No crossover point found in any of the runs.")
