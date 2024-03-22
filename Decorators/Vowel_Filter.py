def vowel_filter(function):
    vowels = "aeoyi"
    def wrapper():
        only_vowels = [el for el in function() if el in vowels]
        return only_vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())