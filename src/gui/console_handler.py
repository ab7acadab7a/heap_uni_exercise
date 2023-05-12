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
        running = True
        while running:
            heap_arr = self.intro()
            if heap_arr == "exit":
                break
            elif heap_arr == "skip":
                print("did you mean to exit()?\n")
                continue
            print(f"heap from input is - {heap_arr}")
            heap = Heap(heap_arr)

    def intro(self) -> list or str:
        print("Maman 13 - tom peleg 209626621\nwelcome to tom's amazing heap application, you can make these actions:")
        input_response = input("1. enter a list of numbers separated by spaces to represent a heap\n"
                               "2. exit by entering exit()\n")
        try:
            return self.handle_intro_input(input_response)
        except Exception as e:
            return "skip"

    @staticmethod
    def handle_intro_input(input_response: str) -> list or str:
        if input_response == "exit()":
            return "exit()"
        numbers_list = input_response.split(" ")
        numbers = []
        for num_str in numbers_list:
            num_str = num_str.strip()
            if num_str:
                num = float(num_str)
                numbers.append(num)
        return numbers
