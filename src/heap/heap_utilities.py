import math


def parent(index: int) -> int:
    """
    Get the index for the parent of the given index
    :param index: a child value's index
    :return: current index's parents index
    """
    return int((index + 1) / 2)


def left(index: int) -> int:
    """
    Return the index of the left value to the given index
    :param index: the current values index
    :return: The index for the value to the left of the given index in the heap
    """
    return index * 2 + 1



def right(index: int) -> int:
    """
    Return the index of the right value to the given index
    :param index: the current values index
    :return: The index for the value to the right of the given index in the heap
    """
    return (index + 1) * 2


def get_level(index: int):
    """
    Get the level value of the given index
    :param index: the index to calculate the level of
    :return: the level of the given index
    """
    return int(math.log(index + 1, 2))