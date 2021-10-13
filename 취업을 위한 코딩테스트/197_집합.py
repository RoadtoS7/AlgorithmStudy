from sys import stdin

input = stdin.readline

N = int(input())
numbers = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in numbers:
        print('Yes', end=' ')
    else:
        print('No', end=' ')
