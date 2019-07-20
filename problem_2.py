
class rot_search:
    def __init___(self):
        self.start_index = 0
        self.stop_index = 0
        self.first_time = True
        self.adjust = 0
        self.input_list_len = 0
def find_pivot(input_list, pivot = 0):
    mid = len(input_list) // 2
    if len(input_list) == 1:
        return pivot
    else:
        if input_list[mid] > input_list[-1]:
            pivot = pivot + mid
            return find_pivot(input_list[mid:], pivot)
        else:
            pivot = pivot - mid
            return find_pivot(input_list[:mid], pivot)

def rotated_array_search(input_list, number, start_index, stop_index, first_time = False):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 2:
        if input_list[0] == number:
            return start_index
        elif input_list[1] == number:
            return stop_index
        else:
            return - 1

    mid_index = len(input_list) // 2

    while first_time:
        #Do this process only in beginning if array is not sorted
        if input_list[-1] > input_list[0]: #sorted
            break
        mid_index = find_pivot(input_list, mid_index)
        if mid_index == -1:
            mid_index = len(input_list) // 2
        break

    left_min = input_list[0]
    left_max = input_list[mid_index - 1]
    right_min = input_list[mid_index]
    right_max = input_list[-1]
    if number >= left_min and number <= left_max:
        return rotated_array_search(input_list[:mid_index], number, start_index, start_index + mid_index - 1, False)
    elif number >= right_min and number <= right_max:
        return rotated_array_search(input_list[mid_index:], number, start_index + mid_index, stop_index, False)
    else:
        return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print(rotated_array_search(input_list, number, 0, len(input_list) - 1, True))
    if linear_search(input_list, number) == rotated_array_search(input_list, number, 0, len(input_list) - 1, True):
        print("Pass")
    else:
        print("Fail")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1, 2, 3, 4, 5], 5])
#Should all say pass
#Corner case is no rotation and it still works as rotated search matches with linear search