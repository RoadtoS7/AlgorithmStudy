N, M = map(int, input().split())

maze = [input()] * N
visited = [[False] * M for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

count = 0


def dfs(x, y, count):
    global min_count
    if x == N - 1 and y == M - 1:
        min_count = min(min_count, count)
        return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny] and maze[nx][ny] == '1':
            visited[nx][ny] = True
            dfs(nx, ny, count + 1)


visited[0][0] = True
min_count = 201
dfs(0, 0, 1)
print(min_count)
