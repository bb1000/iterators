class Counter:
    def __init__(self, size):
        print("__init__:", size)
        self.size = size
        self.start = 0

    def __iter__(self):
        print("__iter__:", self.size)
        return CounterIter(self.start, self.size)


class CounterIter:

    def __init__(self, start, size):
        self.start = start
        self.size = size

    def __next__(self):
        if self.start < self.size:
            self.start = self.start + 1
            return self.start
        raise StopIteration
