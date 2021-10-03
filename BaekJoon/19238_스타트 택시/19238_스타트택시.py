from collections import deque
from sys import stdin, exit


input = stdin.readline

N, M, oil = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

r, c = map(int, input().split())
r -= 1
c -= 1

d = [[] for _ in range(M + 2)]
for i in range(M):
    sr, sc, tr, tc = map(int, input().split())
    graph[sr - 1][sc - 1] = i + 2
    d[i + 2] = (tr - 1, tc - 1)

dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def move_to_nearest(r, c):
    global oil
    need_visit = deque([(r, c)])
    visited = [[False] * N for _ in range(N)]
    visited[r][c], cnt = True, 0

    while need_visit:
        len_need_visit = len(need_visit)
        p = []
        cnt += 1
        if cnt > oil:
            return -1

        for _ in range(len_need_visit):
            new_r, new_c = need_visit.popleft()

            for dr, dc in dir:
                nr, nc = new_r + dr, new_c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if graph[nr][nc] != 1 and not visited[nr][nc]:
                        if graph[nr][nc] > 1:
                            p.append((nr, nc))
                        visited[nr][nc] = True
                        need_visit.append((nr, nc))

        if p:
            break

    if not p:
        return -1

    cr, cc = sorted(p)[0]
    tr, tc = d[graph[cr][cc]]
    oil -= cnt
    _oil = drive(cr, cc, tr, tc)
    if _oil == -1:
        return -1
    oil += _oil
    graph[cr][cc] = 0
    return tr, tc


def drive(sr, sc, tr, tc):
    need_visit = deque([(sr, sc)])
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0

    while need_visit:
        r, c  = need_visit.popleft()

        if visited[r][c] >= oil:
            return -1

        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] != 1 and visited[nr][nc] == -1:
                need_visit.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if nr == tr and nc == tc:
                    return visited[nr][nc]
    return -1


for _ in range(M):
    ## 다음으로 이동하는
    if graph[r][c] > 0:
        tr, tc = d[graph[r][c]]
        _oil = drive(r, c, tr, tc)
        if _oil == -1:
            print(-1)
            exit(0)

        oil += _oil
        graph[r][c] = 0
        r, c = tr, tc
        continue

    result = move_to_nearest(r, c)
    if result == -1:
        print(-1)
        exit(0)
    else:
        r, c = result

print(oil)




