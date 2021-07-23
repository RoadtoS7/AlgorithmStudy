N, M = map(int, input().split())

result = 0
visited = [[False] * N for _ in range(N)]
need_visit = []
graph = []
counts = []

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(M):
    graph.append(input())

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and not visited[i][j]:
            result += 1
            count = 0
            need_visit.append((i, j))
            while need_visit:
                x, y = need_visit.pop()
                if graph[x][y] == '1' and not visited[x][y]:
                    visited[x][y] = True
                    count += 1
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue
                        if graph[nx][ny] == '1' and not visited[nx][ny]:
                            need_visit.append((nx, ny))
            counts.append(count)

counts.sort()
print(result)
for count in counts:
    print(count, end='\n')
