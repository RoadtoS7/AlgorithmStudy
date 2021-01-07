import math
n = int(input())

array = [0] * n
for i in range(n):
    array[i] = int(input())

array.sort()

result = 0
for i in range(n):
    result += abs(array[i] - (i + 1))
print(result)