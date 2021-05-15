from sys import stdin
from collections import deque
input = stdin.readline

T = int(input().strip())

for _ in range(T):
    operators = input().strip()
    N = int(input().strip())

    nums = []
    if N > 0:
        nums = deque(map(int, input().lstrip('[').rstrip(']\n').split(',')))
    else:
        input()

    operators.replace('RR', '')
    if operators.count('D') > N or (operators.count('D') > 0 and not nums):
        print('error')
        continue

    k = 0
    right = True
    while k < len(operators):
        if operators[k] == 'R':
            right = not right
            k += 1
            continue

        if right:
            nums.popleft()
        else:
            nums.pop()
        k += 1

    if not right:
        nums.reverse()
    print(str(list(nums)).replace(' ', ''))


