## p149
## BFS
from collections import deque

N, M = map(int, input().split())

graph = []
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(N):
    row = list(map(int, input()))
    graph.append(row)

count = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] != 1:
            count += 1
            need_visit = deque([(r, c)])

            while need_visit:
                node_r, node_c = need_visit.popleft()
                graph[node_r][node_c] = 1

                for dr, dc in dir:
                    new_r, new_c = node_r + dr, node_c + dc

                    if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c] != 1:
                        need_visit.append((new_r, new_c))

print(count)



