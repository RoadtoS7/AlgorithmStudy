n = int(input())
number = [0] * 10001

for _ in range(n):
    index = int(input())
    number[index] += 1

for index in range(1, 10001):
    if index != 0:
        for i in range(number[index]):
            print(index)
