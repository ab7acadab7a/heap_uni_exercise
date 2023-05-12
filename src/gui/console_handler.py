import json
from curses.ascii import isalpha

from src.heap.heap import Heap


def load_json_configuration(path: str):
    """
    Load a configuration file that is of json type
    :param path: the path for this file
    :return: a list that will be the heap data
    """
    with open(path) as f:
        return json.load(f)


class ConsoleHandler:

    def __init__(self, path: str = None):
        data_arr = load_json_configuration(path)
        self.heap = Heap(data_arr)

    def run(self):
        running = True
        while running:
            heap_arr = self.intro()
            if heap_arr == "exit":
                break
            elif heap_arr == "skip":
                continue
            print(f"heap from input is - {heap_arr}")
            heap = Heap(heap_arr)

    @staticmethod
    def intro() -> list or str:
        print("Maman 13 - tom peleg 209626621\nwelcome to tom's amazing heap application, you can make these actions:")
        numbers_str = input("1. enter a list of numbers separated by spaces to represent a heap\n"
                            "2. exit by entering exit()")
        if numbers_str == "exit()":
            return "exit()"
        elif isalpha(numbers_str):
            return "skip"
        numbers_list = numbers_str.split(" ")
        numbers = []
        for num_str in numbers_list:
            num_str = num_str.strip()
            if num_str:
                num = float(num_str)
                numbers.append(num)
        return numbers
