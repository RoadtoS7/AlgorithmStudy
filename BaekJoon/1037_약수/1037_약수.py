N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print(numbers[0] ** 2)
else:
    numbers.sort()
    print(numbers[0] * numbers[-1])