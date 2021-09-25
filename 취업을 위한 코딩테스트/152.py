from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())

graph = []
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip('\n')))))

def bfs(start_r, start_c):
    min_length = 1e9
    need_visit = deque([(start_r, start_c, 1)])


    while need_visit:
        node_r, node_c, length = need_visit.popleft()
        graph[node_r][node_c] = 0

        if node_r == N - 1 and node_c == M - 1:
            min_length = min(min_length, length)



        for dr, dc in dir:
            new_r, new_c = node_r + dr, node_c + dc

            if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c] == 1:
                need_visit.append((new_r, new_c, length + 1))

    return min_length

print(bfs(0, 0))







