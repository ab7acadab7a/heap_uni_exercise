import json
import os.path

from heap import Heap


class ConsoleHandler:

    def __init__(self, root_path: str = None):
        # Use given root path or just get it based on the dir
        self.root_path = root_path or os.path.dirname(os.path.abspath(__file__))
        self.running = False

        # Empty init
        self.heap = Heap([])
        self.intro_function_menu = self.initialize_intro_menu()
        self.current_menu = self.intro_function_menu
        self.functions_menu = self.initialize_function_menu()

    def initialize_intro_menu(self) -> dict:
        return {
            "1": [self.console_heap_input, "input a heap using the console"],
            "2": [self.load_json_configuration, "input a heap using a .json file"],
            "q": [self.exit, "exit the program"],
        }

    def initialize_function_menu(self) -> dict:
        return {
            "1": [self.activate_build_heap, "build heap"],
            "2": [self.activate_heapify, "heapify"],
            "3": [self.heap.heap_extract_max, "heap extract max"],
            "4": [self.heap.heap_extract_min, "heap extract min"],
            "5": [self.activate_insert, "heap insert"],
            "6": [self.activate_delete, "heap delete"],
            "p": [self.heap.print_heap, "print heap"],
            "b": [self.switch_intro_menu, "go back to the first menu"],
            "q": [self.exit, "exit the program"],
        }

    def activate_build_heap(self):
        print("building heap...")
        self.heap.build_heap()
        self.heap.print_heap()

    def activate_heapify(self):
        index = input("please enter the index to heapify\n")
        try:
            self.heap.heapify(int(index))
        except Exception as e:
            print("oops didn't enter index for heapify correctly\n")

    def activate_insert(self):
        value = input("please enter the value to insert into the heap\n")
        try:
            self.heap.heap_insert(int(value))
        except Exception as e:
            print("oops didn't enter value to insert correctly\n")

    def activate_delete(self):
        index = input("please enter the index to delete from the heap\n")
        try:
            self.heap.heap_delete(int(index))
        except Exception as e:
            print("oops didn't enter index to delete from heap correctly\n")

    def run(self):
        self.running = True
        print("Maman 13 - tom peleg 209626621\n"
              "welcome to tom's amazing heap application, input a number to make these actions:")
        while self.running:
            self.print_current_menu()
            input_response = self.await_selection_input()
            if input_response == "skip": continue
            self.current_menu[input_response][0]()

    def await_selection_input(self):
        input_response = input("choose from the above:\n")
        if input_response in self.current_menu.keys():
            return input_response
        else:
            print("oops it seems you didn't pick from the options above")
            return "skip"

    def console_heap_input(self) -> list or str:
        input_response = input("please enter the heap arr in this format\n[number,number,number,number ...]\n")
        try:
            numbers = json.loads(input_response)
            self.heap = Heap(numbers)
            self.functions_menu = self.initialize_function_menu()
            self.current_menu = self.functions_menu
        except Exception as e:
            print("didnt enter correct format, please try again and follow the format\n")

    def print_current_menu(self) -> None:
        print()
        for key in self.current_menu.keys():
            print(f"{key}. {self.current_menu[key][1]}")

    def exit(self):
        print("ok exiting now bye bye")
        self.running = False

    def switch_intro_menu(self):
        self.intro_function_menu = self.initialize_intro_menu()
        self.current_menu = self.intro_function_menu

    def load_json_configuration(self):
        """
        Load a configuration file that is of json type
        :param path: the path for this file
        :return: a list that will be the heap data
        """
        try:
            file_input = input("please write the file name in relative path to /src file:\n")
            with open(os.path.join(self.root_path, file_input)) as f:
                self.heap = Heap(json.load(f))
                print("successfully read from the given path")
        except FileNotFoundError as e:
            print(f"\n file {file_input} not found :( \n")
            return "skip"
