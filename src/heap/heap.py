import math


class Heap:

    def __init__(self, heap_arr: list):
        self.heap = heap_arr

    @staticmethod
    def parent(index: int) -> int:
        """
        Get the index for the parent of the given index
        :param index: a child value's index
        :return: current index's parents index
        """
        return int(index / 2)

    @staticmethod
    def left(index: int) -> int:
        """
        Return the index of the left value to the given index
        :param index: the current values index
        :return: The index for the value to the left of the given index in the heap
        """
        return index * 2

    @staticmethod
    def right(index: int) -> int:
        """
        Return the index of the right value to the given index
        :param index: the current values index
        :return: The index for the value to the right of the given index in the heap
        """
        return index * 2 + 1

    @staticmethod
    def get_level(index: int):
        """
        Get the level value of the given index
        :param index: the index to calculate the level of
        :return: the level of the given index
        """
        return int(math.log(index, 2))

    def heap_extract_max(self):
        """
        :return: The biggest value in the heap if there are values in the heap
        """
        return self.heap[0] if len(self.heap) > 0 else "no values in heap"

    def heap_extract_min(self):
        """
        :return: The biggest value in the heap if there are values in the heap
        """
        # First value in the heap will be the biggest and smallest if its the only value
        if len(self.heap) == 0:
            return "no values in heap"
        elif len(self.heap) == 1:
            return self.heap[0]
        # there is more then 1 value
        if self.is_valid_index(2) and self.heap[1] > self.heap[2]:
            return self.heap[2]
        return self.heap[1]

    def heapify(self, index: int) -> None:
        """
        Heapify the heaps array based on the given index and the level its in
        :param index: Current index of heap to heapify
        :return:
        """
        if self.is_leaf(index):
            return

        if self.get_level(index) % 2 == 0:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def is_leaf(self, index: int) -> bool:
        """
        Check if given index is a list in the heap
        :param index: the index to check
        :return: if the index is a leaf or not
        """
        return self.right(index) > len(self.heap) and self.left(index) > len(self.heap)

    def swap(self, index: int, swapped: int) -> None:
        """
        Swap the values of the given indexes in inner eap
        :param index: some legal index in the heap
        :param swapped: some other legal index in the heap
        """
        temp_value = self.heap[index]
        self.heap[index] = self.heap[swapped]
        self.heap[swapped] = temp_value

    def max_heap_compare(self, index: int, suspect: int) -> bool:
        """
        Function to compare 2 indexes that could be in the heap and return true if the suspect is bigger
        :param index: some index
        :param suspect: potential index to be bigger then the index
        :return: true if the suspect index has a bigger value and is valid
        """
        return suspect <= len(self.heap) and self.heap[suspect] > self.heap[index]

    def min_heap_compare(self, index: int, suspect: int) -> bool:
        """
        Function to compare 2 indexes that could be in the heap and return true if the suspect is smaller
        :param index: some index
        :param suspect: potential index to be smaller then the index
        :return: true if the suspect index has a smaller value and is valid
        """
        return suspect <= len(self.heap) and self.heap[suspect] < self.heap[index]

    def is_valid_index(self, index: int) -> bool:
        """
        Determine if a given index is a valid one based on the heap
        :param index: Some index
        :return: Bool based on validity of index to the heap
        """
        return index <= len(self.heap)

    def possible_grandchildren(self, index: int) -> list:
        """
        Given an index return a list of the grandchildren
        :param index: some valid index in the heap
        :return: a list of the possible grandchildren indexes
        """
        # Get the possible grandchildren of the given index
        return [self.right(self.right(index)), self.left(self.right(index)),
                self.right(self.left(index)), self.left(self.left(index))]

    def full_family(self, index: int) -> list:
        """
        Return the full children and grandchildren of a given index, while ignoring invalid indexes
        """
        possible_indexes = [self.right(index), self.left(index)] + self.possible_grandchildren(index)

        # Return the valid indexes out of the possible ones
        return [grandchild for grandchild in possible_indexes if self.is_valid_index(grandchild)]

    def choose_heap_next_best_index(self, index: int, compare) -> int:
        """
        This function takes an index and a function and chooses the next bext index based on the compare function
        the options should be an index, its children and grandchildren
        :param index: some index to check
        :param compare: a compare function to check with between all the indexes
        :return: the next best index based on the compare function
        """
        possibles = self.full_family(index)

        possibles.sort(key=compare, reverse=not self.get_level(index) % 2)

        # Get the first value
        return possibles[0]

    def get_value(self, index: int) -> int:
        return self.heap[index]

    def max_heapify(self, index: int) -> None:
        """
        Max heapify the current index value according to the sub tree values,
        Call when finished, because of the assignment call the min heapify function to handle next level heap
        :param index: some index
        """

        largest = self.choose_heap_next_best_index(index, self.get_value)

        # Check if heap is valid or not - meaning did some child happen to be bigger then current value
        if largest != index:
            self.swap(index, largest)
            # Since we are working with max_min heap we need to call the min heap on the next level
            self.min_heapify(largest)

    def min_heapify(self, index: int) -> None:
        """
        Min heapify the current index value according to the sub tree values,
        Call when finished, because of the assignment call the min heapify function to handle next level heap
        :param index: some index
        """
        # left = self.left(index)
        # right = self.right(index)

        largest = self.choose_heap_next_best_index(index, self.get_value)

        # Check that left index is valid and bigger then current value
        # if self.max_heap_compare(index, left):
        #     largest = left
        # else:
        #     largest = index
        #
        # # Check if right index is valid and bigger then current value
        # if self.max_heap_compare(largest, right):
        #     largest = right

        # Check if heap is valid or not - meaning did some child happen to be bigger then current value
        if largest != index:
            self.swap(index, largest)
            # Since we are working with max_min heap we need to call the min heap on the next level
            self.max_heapify(largest)