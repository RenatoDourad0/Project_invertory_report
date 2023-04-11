from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.current = 0
        self.data = data

    def __next__(self):
        try:
            if self.current < 0:
                raise IndexError()
            data = self.data[self.current]
        except IndexError:
            raise StopIteration()
        else:
            self.current += 1
        return data
