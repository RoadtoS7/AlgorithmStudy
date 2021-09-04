from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
last_virus = [[] for _ in range(K + 1)]

graph = []
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] > 0:
            last_virus[row[j]].append((i, j))

S, X, Y = list(map(int, input().split()))
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for _ in range(S):
    for i in range(1, K + 1):
        last_locations = last_virus[i]
        last_virus[i] = []
        for r, c in last_locations:
            for dr, dc in dir:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < N and 0 <= new_c < N and graph[new_r][new_c] == 0:
                    graph[new_r][new_c] = i
                    last_virus[i].append((new_r, new_c))

print(graph[X - 1][Y - 1])











