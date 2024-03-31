class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.last_index = len(self.collection)
        self.first_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.last_index -= 1
        if self.last_index < self.first_index:
            raise StopIteration()
        return self.collection[self.last_index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list: print(item)
