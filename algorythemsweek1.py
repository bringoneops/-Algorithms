#!/usr/bin/python3

# Pseudocode for Selection Sort:
# SelectionSort(A):
#     for i from 0 to length(A) - 2
#         // Find the minimum element in unsorted array
#         minIndex = i
#         for j from i + 1 to length(A) - 1
#             if A[j] < A[minIndex]
#                 minIndex = j
#         // Swap the found minimum element with the first element
#         if minIndex != i
#             swap A[i] with A[minIndex]


def selection_sort(A):
    n = len(A)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]


# Example array
A = [64, 25, 12, 22, 11]
selection_sort(A)
print("Sorted array is:", A)
