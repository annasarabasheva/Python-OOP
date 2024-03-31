class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "o", "u", "e", "y", "i"]
        self.first_index = -1
        self.last_index = len(self.text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.first_index += 1
        if self.first_index > self.last_index:
            raise StopIteration()
        if self.text[self.first_index].lower() in self.vowels:
            return self.text[self.first_index]
        return self.__next__()





my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)