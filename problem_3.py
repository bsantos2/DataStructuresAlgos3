class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0  # denotes next index where new element should go

    def heapify(self):
        # take last node then heapify
        curr_idx = self.next_index
        # parent index
        while curr_idx >= 1:
            parent_idx = (curr_idx - 1) // 2
            if self.cbt[curr_idx] < self.cbt[parent_idx]:
                dummy = self.cbt[curr_idx]
                self.cbt[curr_idx] = self.cbt[parent_idx]
                self.cbt[parent_idx] = dummy
                curr_idx = parent_idx
            else:
                return

    def insert(self, data):
        """
        Insert `data` into the heap
        """
        self.cbt[self.next_index] = data
        self.heapify()
        self.next_index += 1
        if self.next_index > len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]
        return

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list:
        sort_list = Heap(len(input_list))
        for x in input_list:
            sort_list.insert(x)

        number1 = 0
        number2 = 0
        for x in range(0, len(sort_list.cbt)):
            if x + 1 < len(sort_list.cbt):
                if sort_list.cbt[x] > sort_list.cbt[x + 1]:
                    dummy = sort_list.cbt[x]
                    sort_list.cbt[x] = sort_list.cbt[x + 1]
                    sort_list.cbt[x + 1] = dummy
            exponent = x // 2
            if x % 2 == 0:
                number1 += sort_list.cbt[x] * 10 ** exponent
            else:
                number2 += sort_list.cbt[x] * 10 ** exponent
        return [number1, number2]
    else:
        print("Input list is empty")
        return [-99999, -99999]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case3 = [[0, 0], [0, 0]]
test_case4 = [[], [-99999, -99999]]
test_function(test_case1)
test_function(test_case2)
test_function(test_case3)
test_function(test_case4)
#All outputs should say pass
#0,0 should yield 0,0 as the corner case
#[] should yield [-99999, -99999], because it's a corner case without relevant result as it's empty
#[] also prints warning message that list is empty
