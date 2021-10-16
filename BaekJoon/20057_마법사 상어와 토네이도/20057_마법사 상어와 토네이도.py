def get_sand_receiver_info(dir):
    if dir == 0: # <-
        res = [
            (-1, 1, 1), (1, 1, 1), # 1퍼센트
            (-1, 0, 7), (1 ,0, 7),
            (-2, 0, 2), (2, 0, 2),
            (-1, -1, 10), (1, -1, 10),
            (0, -2, 5)
        ]
    elif dir == 1: # 아래 방향
        res = [
            (-1, -1, 1), (-1, 1, 1),
            (0, -1, 7), (0, 1, 7),
            (0, -2, 2), (0, 2, 2),
            (1, -1, 10), (1, 1, 10),
            (2, 0, 5)
        ]
    elif dir == 2: #  ->
        res = [
            (-1, -1, 1), (1, -1, 1),
            (1, 0, 7), (-1, 0, 7),
            (2, 0, 2), (-2, 0, 2),
            (-1, 1, 10), (1, 1, 10),
            (0, 2, 5)
        ]
    elif dir == 3: # 윗 방향
        res = [
            (1, -1, 1), (1, 1, 1),
            (0, -1, 7), (0, 1, 7),
            (0, -2, 2), (0, 2, 2),
            (-1, -1, 10), (-1, 1, 10),
            (-2, 0, 5)
        ]
    return res

# 입력 y좌표
def get_a(yr, yc, dir):
    if dir == 0:
        yc -= 1

    elif dir == 1:
        yr += 1

    elif dir == 2:
        yc += 1
    elif dir == 3:
        yr -= 1

    return yr, yc

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
dir = 0
r, c = N // 2, N // 2
l, lcount = 1, 0
loss_sand = 0

while r != 0 or c != 0:
    for _ in range(l):
        r, c = r + dr[dir], c + dc[dir]

        if graph[r][c] == 0:
            continue

        ssum = 0
        for sdr, sdc, per in get_sand_receiver_info(dir):
            nr, nc = r + sdr, c + sdc

            sand = int((graph[r][c] / 100) * per)
            ssum += sand
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                loss_sand += sand
            else:
                graph[nr][nc] += sand

        ## a좌표 모래 할당
        ar, ac = get_a(r, c, dir)
        if ar < 0 or ar >= N or ac < 0 or ac >= N:
            loss_sand += (graph[r][c] - ssum)
        else:
            graph[ar][ac] += graph[r][c] - ssum

        graph[r][c] = 0

    lcount += 1
    if lcount >= 2 and l < N - 1:
        l += 1
        lcount = 0

    dir = (dir + 1) % 4


print(loss_sand)








