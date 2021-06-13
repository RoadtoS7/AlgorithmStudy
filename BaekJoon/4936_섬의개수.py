import sys
sys.setrecursionlimit(100000)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]


def dfs(x, y):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= h or ny >= w:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    count = 0
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1 and not visited[x][y]:
                count += 1
                dfs(x, y)

    print(count)
