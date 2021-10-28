N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

max_value = -1
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dir_x = [
    [(0, 1), (0, -1), (1, 0)],
    [(0, 1), (0, -1), (-1, 0)],
    [(0, 1), (1, 0), (-1, 0)],
    [(0, -1), (1, 0), (-1, 0)],
]

visited = [[False] * M for _ in range(N)]


def dfs(r, c, count, value):
    global max_value

    if count >= 4:
        max_value = max(max_value, value)
        return

    for dr, dc in dir:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc, count + 1, value + graph[nr][nc])
                visited[nr][nc] = False


for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, graph[r][c])
        visited[r][c] = False

for r in range(N):
    for c in range(M):

        for dir in dir_x:
            value = graph[r][c]
            is_ok = True
            for dr, dc in dir:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < M:
                    value += graph[nr][nc]
                else:
                    is_ok = False

            if is_ok:
                max_value = max(max_value, value)

print(max_value)
