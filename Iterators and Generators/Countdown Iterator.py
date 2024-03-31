class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current < 0:
            raise StopIteration
        return self.current






iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")