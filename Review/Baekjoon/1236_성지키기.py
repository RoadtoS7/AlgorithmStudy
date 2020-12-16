n, m = map(int, input().split(' '))

row = [0] * n
column = [0] * m
array = []

for _ in range(n):
    array.append(input())

for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_result = 0
for i in range(n):
    if row[i] == 0:
        row_result += 1

column_result = 0
for j in range(m):
    if column[j] == 0:
        column_result += 1

print(max(row_result, column_result))