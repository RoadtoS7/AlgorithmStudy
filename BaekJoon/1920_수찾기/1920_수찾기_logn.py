from sys import stdin
input = stdin.readline
def is_exist(numbers, target):
    start, end = 0, len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] < target:
            start = mid + 1
        elif numbers[mid] > target:
            end = mid - 1
        else:
            return 1
    return 0


N, numbers = int(input()), list(map(int, input().rstrip('\n').split()))
M, targets = int(input()), list(map(int, input().rstrip('\n').split()))

numbers.sort()
for target in targets:
    print(is_exist(numbers, target))
