from flat_iterator import FlatIterator
from flat_generator import flat_generator
from pprint import pprint
from typing import Any


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)  #

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print(list(flat_generator(nested_list)))

    for item in flat_generator(nested_list):
        print(item)
