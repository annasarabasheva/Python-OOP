def create_rhombus(n):
    print(' ' * (n - i), end='')
    print("* " * i)


n = int(input())

for i in range(1, n + 1):
    create_rhombus(n)

for i in range(n-1, 0, -1):
    create_rhombus(n)