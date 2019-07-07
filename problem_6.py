def get_min_max(ints):
    result = merge_sort(ints)
    minmax = (result[0], result[-1])
    return minmax

def merge_sort(ints):
    if len(ints) <= 1:
        return ints
    midpoint = len(ints) // 2
    left = ints[:midpoint]
    right = ints[(midpoint):]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge_some(left, right)

def merge_some(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

## Example Test Case of Ten Integers
import random

for k in range (0, 4):
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Trial" + str(k) + "\n")
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")