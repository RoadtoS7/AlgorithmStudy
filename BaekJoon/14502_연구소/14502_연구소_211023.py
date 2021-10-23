from copy import deepcopy
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

viruses = []
empty_lst = []
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for r in range(N):
    for c in range(M):
        if graph[r][c] == 2:
            viruses.append((r, c))
        if graph[r][c] == 0:
            empty_lst.append((r, c))

def put_wall(wall_list):
    new_graph = deepcopy(graph)
    for r, c in wall_list:
        new_graph[r][c] = 1
    return new_graph

def bfs(graph):
    need_visit = deque(deepcopy(viruses))

    while need_visit:
        r, c = need_visit.popleft()

        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                graph[nr][nc] = 1
                need_visit.append((nr, nc))

def calc_safe_area(graph):
    count = 0
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                count += 1

    return count

res = -1
for lst in combinations(empty_lst, 3):
    new_graph = put_wall(lst)
    bfs(new_graph)
    value = calc_safe_area(new_graph)
    res =  max(res, value)

print(res)


