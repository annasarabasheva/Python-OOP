value = input()

if value[0] != '0' or len(value) != 10 or not value.isnumeric():
    raise ValueError("Invalid phone number!")
else:
    print('ok')