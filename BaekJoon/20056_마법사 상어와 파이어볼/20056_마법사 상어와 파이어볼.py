N, M, K = map(int, input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]

fires = [list(map(int, input().split())) for _ in range(M)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for r, c, m, s, d in fires:
    graph[r - 1][c - 1].append((m, s, d))


def move_fire(graph):
    temp = []
    for r in range(N):
        for c in range(N):
            for _ in range(len(graph[r][c])):
                m, s, d = graph[r][c].pop()
                nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
                temp.append((nr, nc, m, s, d))

    for r, c, m, s, d in temp:
        graph[r][c].append((m, s, d))


def merge_fire(graph):
    all_even_odd_dir = [0, 2, 4, 6]
    all_not_even_dir = [1, 3, 5, 7]

    for r in range(N):
        for c in range(N):
            fire_count = len(graph[r][c])
            tmp = []

            if fire_count >= 2:
                is_even = False
                is_odd = False

                total_m, total_s = 0, 0
                for m, s, d in graph[r][c]:
                    if d % 2 == 1:
                        is_odd = True
                    else:
                        is_even = True

                    total_m += m
                    total_s += s

                one_m = total_m // 5
                one_s = total_s // fire_count
                graph[r][c] = []
                if one_m == 0:
                    continue

                if is_odd and is_even:
                    for d in all_not_even_dir:
                        graph[r][c].append((one_m, one_s, d))
                else:
                    for d in all_even_odd_dir:
                        graph[r][c].append((one_m, one_s, d))


for _ in range(K):
    move_fire(graph)
    merge_fire(graph)

res = 0
for r in range(N):
    for c in range(N):
        if len(graph[r][c]) > 0:
            for m, s, d in graph[r][c]:
                res += m

print(res)
