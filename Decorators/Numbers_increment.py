def number_increment(numbers):
    def increase():
        increased_numbers = [num + 1 for num in numbers]
        return increased_numbers

    return increase()


print(number_increment([1, 2, 3]))