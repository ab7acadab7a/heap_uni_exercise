import json

from src.heap.heap import Heap


def load_json_configuration(path: str):
    """
    Load a configuration file that is of json type
    :param path: the path for this file
    :return: a list that will be the heap data
    """
    with open(path) as f:
        return json.load(f)["heap_arr"]


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
            heap = Heap(heap_arr)
            print(f"heap from input is - {heap.heap}")
            while running:
                response = self.main_functions()
                if response == "6":
                    running = False
                    break


    def intro(self) -> list or str:
        print("Maman 13 - tom peleg 209626621\n"
              "welcome to tom's amazing heap application, input a number to make these actions:")
        input_response = input("1. enter a list of numbers separated by spaces to represent a heap\n"
                               "2. exit\n")
        try:
            if input_response == "1":
                return self.handle_intro_input()
            if input_response == "2":
                return "exit()"
        except Exception as e:
            return "skip"

    @staticmethod
    def main_functions() -> str:
        return input("here are the main functions you can do on this heap.\n"
                     "enter the number of the command you want to execute:\n"
                     "1. heapify\n"
                     "2. heap_insert\n"
                     "3. heap_extract_min\n"
                     "4. heap_extract_max\n"
                     "5. heap_delete\n"
                     "6. exit\n")

    @staticmethod
    def handle_intro_input() -> list or str:
        input_response = input("please enter the numbers of the heap separated by spaces\n")
        numbers_list = input_response.split(" ")
        numbers = []
        for num_str in numbers_list:
            num_str = num_str.strip()
            if num_str:
                num = float(num_str)
                numbers.append(num)
        return numbers
