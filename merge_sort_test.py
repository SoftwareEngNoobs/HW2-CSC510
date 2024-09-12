## Test Cases 

import hw2_debugging, rand

def test_merge_random():
    arr = rand.random_array([0] * 20)
    assert hw2_debugging.merge_sort(arr) == sorted(arr)

def test_merge_reversed_array():
    arr = sorted(rand.random_array([0] * 20))[::-1]
    assert hw2_debugging.merge_sort(arr) == arr[::-1]
