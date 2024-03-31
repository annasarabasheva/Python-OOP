def reverse_text(word):
    first_index = 0
    last_index = len(word) - 1
    while last_index >=  first_index:
        yield word[last_index]
        last_index -= 1


for char in reverse_text("step"):
    print(char, end='')
