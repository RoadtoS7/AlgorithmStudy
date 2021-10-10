import sys

sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True

    for dr, dc in dir:
        new_r, new_c = x + dr, y + dc

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
            continue

        if graph[new_r][new_c] and not visited[new_r][new_c]:
            dfs(new_r, new_c)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        graph[r][c] = 1



    count = 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
