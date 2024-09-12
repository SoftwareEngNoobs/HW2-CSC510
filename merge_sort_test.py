## Test Cases 

import hw2_debugging, rand

def test_merge_random():
    arr = rand.random_array([0] * 20)
    assert hw2_debugging.merge_sort(arr) == sorted(arr)

def test_merge_reversed_array():
    # Test with an array that is sorted in descending order
    arr = sorted(rand.random_array([0] * 20))[::-1]
    assert hw2_debugging.merge_sort(arr) == arr[::-1]
    
def test_duplicates():
     # Test with an array that has duplicate elements
    assert hw2_debugging.merge_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8], "Sorting an array with duplicates FAILED"
