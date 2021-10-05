from sys import stdin
from collections import deque

input = stdin.readline


def max_area_count(graph, length):
    max_count = -1

    for i in range(length):
        for j in range(length):
            if graph[i][j] > 0:
                count = 0
                need_visit = deque([(i, j)])

                while need_visit:
                    r, c = need_visit.popleft()
                    if graph[r][c] > 0:
                        graph[r][c] = 0
                        count += 1

                    for dr, dc in dir:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < length and 0 <= nc < length:
                            if graph[nr][nc] > 0:
                                need_visit.append((nr, nc))

                max_count = max(max_count, count)
    return max_count


def solution(L, length):
    for l in L:
        k = 2 ** l
        # 회전
        for x in range(0, length, k):
            for y in range(0, length, k):
                tmp = [graph[i][y:y + k] for i in range(x, x + k)]
                for i in range(k):
                    for j in range(k):
                        graph[x + j][y + k - 1 - i] = tmp[i][j]


        need_minus = []
        ## 주변 얼음 개수 카운팅
        for r in range(length):
            for c in range(length):
                if graph[r][c] <= 0:
                    continue

                count = 0
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < length and 0 <= nc < length and graph[nr][nc]:
                        count += 1

                if count < 3 and graph[r][c]:
                    need_minus.append((r, c))

        for r, c in need_minus:
            graph[r][c] -= 1


    print(sum(sum(ar) for ar in graph))
    print(max_area_count(graph, length))


N, Q = map(int, input().split())
graph = []
for i in range(2 ** N):
    graph.append(list(map(int, input().split())))

L = list(map(int, input().split()))
dir = [(1, 0), (0, -1), (0, 1), (-1, 0)]
solution(L, len(graph))
