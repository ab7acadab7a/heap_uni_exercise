import math

from src.heap.heap_utilities import right, left, get_level, possible_grandchildren


class Heap:

    def __init__(self, heap_arr: list):
        self.heap = heap_arr
        self.build_heap()

    def heap_extract_max(self):
        """
        :return: The biggest value in the heap if there are values in the heap
        """
        found_value = self.heap[0] if len(self.heap) > 0 else "no values in heap"
        print(f"found maximum value - {found_value}")
        return found_value

    def heap_extract_min(self) -> int or str:
        """
        :return: The biggest value in the heap if there are values in the heap
        """
        # First value in the heap will be the biggest and smallest if its the only value
        if len(self.heap) == 0:
            found_value = "no values in heap"
        elif len(self.heap) == 1:
            found_value = self.heap[0]
        # there is more then 1 value
        elif self.is_valid_index(2) and self.heap[1] > self.heap[2]:
            found_value = self.heap[2]
        else:
            found_value = self.heap[1]
        print(f"found minimum value - {found_value}")
        return found_value

    def heapify(self, index: int) -> None:
        """
        Heapify the heaps array based on the given index and the level its in
        :param index: Current index of heap to heapify
        :return:
        """
        if self.is_leaf(index):
            return

        if get_level(index) % 2 == 0:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def is_leaf(self, index: int) -> bool:
        """
        Check if given index is a list in the heap
        :param index: the index to check
        :return: if the index is a leaf or not
        """
        return right(index) > len(self.heap) and left(index) > len(self.heap)

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
        return index < len(self.heap)

    def build_heap(self):
        """
        iterate the heap from the last item that is not at the last depth
        and start heapifing backwards
        """
        heap_size = len(self.heap)
        start = int(heap_size / 2) - 1  # first none last depth item
        for i in range(start, -1, -1):
            self.heapify(i)
            self.heapify(right(i))
            self.heapify(left(i))

    def full_family(self, index: int) -> list:
        """
        Return the full children and grandchildren of a given index, while ignoring invalid indexes
        """
        possible_indexes = [right(index), left(index), index] + possible_grandchildren(index)

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

        possibles.sort(key=compare, reverse=not get_level(index) % 2)

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
            self.heapify(largest)

    def min_heapify(self, index: int) -> None:
        """
        Min heapify the current index value according to the sub tree values,
        Call when finished, because of the assignment call the min heapify function to handle next level heap
        :param index: some index
        """
        # left = self.left(index)
        # right = self.right(index)

        smallest = self.choose_heap_next_best_index(index, self.get_value)

        # Check if heap is valid or not - meaning did some child happen to be bigger then current value
        if smallest != index:
            self.swap(index, smallest)
            # Since we are working with max_min heap we need to call the min heap on the next level
            self.heapify(smallest)

    def print_heap(self):
        """
        Prints the elements of a heap in a tree-like format.
        """
        n = len(self.heap)
        max_level = (n - 2) // 2  # last level that is not a leaf

        # Determine the length of the largest number in the heap
        max_length = len(str(max(self.heap)))

        # Print each level of the heap
        for level in range(max_level + 1):
            start = 2 ** level - 1  # index of first node in level
            end = min(start + 2 ** level, n)  # index of last node in level
            spacing = 2 ** (max_level - level) - 1  # spacing between nodes in level

            # Print the nodes in the level
            for i in range(start, end):
                node_str = str(self.heap[i]).center(max_length)
                print(" " * (spacing * max_length), node_str, end="")
                spacing = 2 ** (max_level - level + 1) - 1

            print()  # move to next line
