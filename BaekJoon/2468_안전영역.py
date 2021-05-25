import sys

sys.setrecursionlimit(100000)
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
max_count = -1


def dfs(x, y, height):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if graph[nx][ny] > height and not visited[nx][ny]:
            dfs(nx, ny, height)


def count_safe_zone(height):
    count = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > height and not visited[i][j]:
                count += 1
                dfs(i, j, height)
    return count

for water in range(0, 100):
    visited = [[False] * N for _ in range(N)]
    safe_zone = count_safe_zone(water)
    max_count = max(safe_zone, max_count)

print(max_count)