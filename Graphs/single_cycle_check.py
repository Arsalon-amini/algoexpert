'''
Given an array of integers where each integer represents a jump of its value in the array. 
Ex. 2 -> rpresents a jump of two indices forward, and -3 represents a jump of three indices backward

Note: if a jump spills past the array's bounds, it wraps to the other side.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle occurs if,
starting at any index in the array and following the jumps, every element in the array is visited exactly once before landing back on starting index.
'''

# input = [2, 3, 1, -4, -4, 2]

'''
input = [2, 3, 1, -4, -4, 2]

                            ^ 

O(n) time | O(1) space where n represents number of elements in input

[-23, 3, 4, 2, 1]
  ^
current_idx = 1
next_idx = (1 + (-23)) % 5 = -22 % 5 = -2
if (next_idx) < 0 (negative) -> add len(array) -> positive idx equivalent
positive_equiv = -2 + 5 = 3 (wrapped around)
'''


def single_cycle_check(array):
    current_idx = 0
    no_elements_visited = 0

    while no_elements_visited < len(array):
        if no_elements_visited > 0 and current_idx == 0:
            return False
        no_elements_visited += 1
        current_idx = get_next_idx(array, current_idx)

    return current_idx == 0


def get_next_idx(array, current_idx):
    jump = array[current_idx]

    next_idx = (current_idx + jump) % len(array)
    return next_idx if next_idx >= 0 else next_idx + len(array)
