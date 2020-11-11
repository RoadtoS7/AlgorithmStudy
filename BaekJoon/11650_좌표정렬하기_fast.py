from sys import stdin
n = int(stdin.readline().rstrip('\n'))
number = [0] * 10001

for _ in range(n):
    index = int(stdin.readline().rstrip('\n'))
    number[index] += 1

for i in range(1, 10001):
    if number[i] != 0:
        for _ in range(number[i]):
            print(i)
