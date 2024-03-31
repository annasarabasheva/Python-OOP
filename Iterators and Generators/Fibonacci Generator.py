def fibonacci():
    current, next = 0, 1
    while True:
        yield current
        current, next = next, current + next


generator = fibonacci()
for i in range(5):
    print(next(generator))