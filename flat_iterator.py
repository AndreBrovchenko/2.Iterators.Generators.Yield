class FlatIterator:

    def __iter__(self):
        self.cursor = 0
        return self

    def __init__(self, input_list):
        self.list = [list_item for internal_list in input_list for list_item in internal_list]

    def __next__(self):
        if self.cursor > len(self.list) - 1:
            raise StopIteration
        list_item = self.list[self.cursor]
        self.cursor += 1
        return list_item
