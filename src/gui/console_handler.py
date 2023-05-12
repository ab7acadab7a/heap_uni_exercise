import json

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
        heap_arr = self.intro()

    @staticmethod
    def intro() -> list:
        print("Maman 13 - tom peleg 209626621\nwelcome to tom's amazing heap application")
        numbers_str = input("Please enter a list of numbers separated by spaces to represent a heap: ")
        numbers_list = numbers_str.split(" ")
        numbers = []
        for num_str in numbers_list:
            num_str = num_str.strip()
            if num_str:
                num = float(num_str)
                numbers.append(num)
        return numbers
