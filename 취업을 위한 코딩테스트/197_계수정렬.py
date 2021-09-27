from sys import stdin

input = stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

is_exist = [False] * (numbers[-1] + 1)
for number in numbers:
    is_exist[number] = True

for target in targets:
    if is_exist[target]:
        print('Yes', end=' ')
    else:
        print('No', end=' ')
