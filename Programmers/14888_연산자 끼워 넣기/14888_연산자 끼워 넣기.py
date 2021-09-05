from sys import stdin
from copy import deepcopy
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def dfs(operators, index, result):
    global max_value, min_value

    if index == N:
        min_value = min(result, min_value)
        max_value = max(result, max_value)
        return

    for i, operator in enumerate(operators):
        new_result = result
        if operator > 0:
            if i == 0:
                new_result = result + numbers[index]
            elif i == 1:
                new_result = result - numbers[index]
            elif i == 2:
                new_result = result * numbers[index]
            elif i == 3:
                if result < 0:
                    new_result  = -((-result) // numbers[index])
                else:
                    new_result = result // numbers[index]

            operators[i] -= 1
            dfs(deepcopy(operators), index + 1, new_result)
            operators[i] += 1

dfs(operators, 1, numbers[0])
print(max_value)
print(min_value)