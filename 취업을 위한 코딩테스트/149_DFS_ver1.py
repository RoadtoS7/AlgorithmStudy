## p149

from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

graph = []

visited = [[False] * M for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip('\n')))))

def dfs(start_r, start_c):
    global visited
    need_visit = [(start_r, start_c)]

    while need_visit:
        node_r, node_c = need_visit.pop()
        if not visited[node_r][node_c]:
            visited[node_r][node_c] = True

            for dr, dc in dir:
                new_r, new_c = node_r + dr, node_c + dc
                if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c] == 0:
                    need_visit.append((new_r, new_c))


count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            count += 1
            dfs(i, j)


print(count)




