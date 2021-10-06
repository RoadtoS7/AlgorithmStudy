from sys import stdin

input = stdin.readline


def get_left_d(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2


def get_back_d(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1


dir = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)}

N, M = map(int, input().split())
x, y, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
count = 1
graph[x][y] = 2


while True:
    nd = d
    for _ in range(4):
        is_all_cleaned = True
        nd = get_left_d(nd)
        dr, dc = dir[nd]
        nx, ny = x + dr, y + dc
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            count += 1
            x, y = nx, ny
            graph[x][y] = 2
            d = nd
            is_all_cleaned = False
            break

    if is_all_cleaned:
        bd = get_back_d(d)
        dr, dc = dir[bd]
        nr, nc = x + dr, y + dc
        if graph[nr][nc] == 1:
            break
        else:
            x, y = nr, nc

print(count)
