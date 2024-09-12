## Test Cases 

import hw2_debugging, rand

def test_merge_random():
    arr = rand.random_array([0] * 20)
    assert hw2_debugging.merge_sort(arr) == sorted(arr)
