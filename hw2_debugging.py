
"""This module consists of two methods that together, perform the Merge Sort algorithm on an array,
returning a sorted array. """
import rand


def merge_sort(array):
    """This function is the parent merge sort algorithm."""
    if len(array) == 1:
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_array, right_array):
    """This function sorts and recombines the two arrays."""
    left_index = 0
    right_index = 0
    merged_array = [None] * (len(left_array) + len(right_array))
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged_array[left_index + right_index] = left_array[left_index]
            left_index += 1
        else:
            merged_array[left_index + right_index] = right_array[right_index]
            right_index += 1

    for i in range(right_index, len(right_array)):
        merged_array[left_index + i] = right_array[i]

    for i in range(left_index, len(left_array)):
        merged_array[i + right_index] = left_array[i]

    return merged_array


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
