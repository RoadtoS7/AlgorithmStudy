import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global result
    visited[x][y] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    array = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0

    for _ in range(K):
        y, x = map(int, input().split())
        array[x][y] = 1

    for i in range(N):
        for j in range(M):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
