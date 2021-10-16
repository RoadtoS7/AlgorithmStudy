from collections import deque
from copy import deepcopy


def move_row_in(graph, dir):
    if dir == 'r_plus':
        for c in range(N):
            already_combined = set()
            for r in range(N - 2, -1, -1):
                if graph[r][c] == 0:
                    continue

                nextr = r + 1
                while nextr < N and graph[nextr][c] == 0:
                    graph[nextr][c] = graph[r][c]
                    graph[r][c] = 0
                    r = nextr
                    nextr += 1

                if nextr < N and nextr not in already_combined and graph[nextr][c] == graph[r][c]:
                    graph[nextr][c] += graph[r][c]
                    graph[r][c] = 0
                    already_combined.add(nextr)

    elif dir == 'r_minus':
        for c in range(N):
            already_combined = set()
            for r in range(1, N):
                if graph[r][c] == 0:
                    continue

                nextr = r - 1
                while nextr >= 0 and graph[nextr][c] == 0:
                    graph[nextr][c] = graph[r][c]
                    graph[r][c] = 0
                    r = nextr
                    nextr -= 1

                if nextr >= 0 and nextr not in already_combined and graph[nextr][c] == graph[r][c]:
                    graph[nextr][c] += graph[r][c]
                    graph[r][c] = 0
                    already_combined.add(nextr)

    return graph


def move_column_in(graph, dir):
    if dir == 'c_plus':
        for r in range(N):
            already_combined = set()
            for c in range(N - 2, -1, -1):
                if graph[r][c] == 0:
                    continue

                next_c = c + 1
                while next_c < N and graph[r][next_c] == 0:
                    graph[r][next_c] = graph[r][c]
                    graph[r][c] = 0
                    c = next_c
                    next_c += 1

                if next_c < N and next_c not in already_combined and graph[r][next_c] == graph[r][c]:
                    graph[r][next_c] += graph[r][c]
                    graph[r][c] = 0
                    already_combined.add(next_c)


    elif dir == 'c_minus':
        for r in range(N):
            already_combined = set()
            for c in range(1, N):
                if graph[r][c] == 0:
                    continue

                next_c = c - 1
                while next_c >= 0 and graph[r][next_c] == 0:
                    graph[r][next_c] = graph[r][c]
                    graph[r][c] = 0
                    c = next_c
                    next_c -= 1

                if next_c >= 0 and next_c not in already_combined and graph[r][next_c] == graph[r][c]:
                    graph[r][next_c] += graph[r][c]
                    graph[r][c] = 0
                    already_combined.add(next_c)
    return graph


def move(graph, dir):
    if dir == 'c_plus' or dir == 'c_minus':
        return move_column_in(graph, dir)
    elif dir == 'r_plus' or dir == 'r_minus':
        return move_row_in(graph, dir)


def bfs(graph):
    need_visit = deque([(graph, 0)])
    max_value = -1

    while need_visit:
        new_graph, count = need_visit.popleft()
        if count == 5:
            new_max_value = max(max(i) for i in new_graph)
            max_value = max(max_value, new_max_value)
            continue

        for d in dir:
            agraph = move(deepcopy(new_graph), d)
            need_visit.append((agraph, count + 1))

    return max_value


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dir = ['c_plus', 'c_minus', 'r_plus', 'r_minus']

res = bfs(graph)
print(res)
