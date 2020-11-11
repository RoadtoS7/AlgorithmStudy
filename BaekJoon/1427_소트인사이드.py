from sys import stdin

number = stdin.readline().rstrip("\n")

for standard in range(9, -1, -1):
    for i in number:
        if int(i) == standard:
            print(i, end='')
