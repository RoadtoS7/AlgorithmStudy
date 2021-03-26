N, M = map(int, input().split())
castle = [input() for _ in range(N)]

is_have_row = [0] * N
is_have_column = [1] * M

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            is_have_row[i] = 1
            is_have_column[j] = 1

row_count = 0
for i in range(N):
    if not is_have_row[i]:
        row_count += 1

column_count = 0
for j in range(M):
    if not is_have_column[j]:
        column_count += 1

print(max(row_count, column_count))
