N, M = map(int, input().split())
castle = [input() for _ in range(N)]

row_need = [0] * N
column_need = [0] * M
for i in range(N):
    for j in range(M):
        if castle[i][j] == '.':
            row_need[i] = 1
            column_need[j] = 1

print(max(sum(row_need), sum(column_need)))
