import itertools

def possible_permutations(lst):
    for permutation in itertools.permutations(lst):
        yield list(permutation)

[print(n) for n in possible_permutations([1, 2, 3])]