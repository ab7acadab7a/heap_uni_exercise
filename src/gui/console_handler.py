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
