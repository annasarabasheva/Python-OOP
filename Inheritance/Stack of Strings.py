class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        result = self.data[::-1]
        return f"[{', '.join(result)}]"



a = Stack()
a.push("baihui")
a.push("zdr")
print(a.__str__())