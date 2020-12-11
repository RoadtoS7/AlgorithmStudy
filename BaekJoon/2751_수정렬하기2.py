n = int(input())

numbers = [0] * n

for i in range(n):
    numbers[i] = int(input())

sorted(numbers)

for i in range(n):
    print(numbers[i])
