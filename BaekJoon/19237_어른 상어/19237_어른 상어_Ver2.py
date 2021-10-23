N, M, K = map(int, input().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))
smell = [[[0, 0]] * N for _ in range(N)]

priorities  = [[] for _ in range(M)]
for i in range(M):
    for _ in range(4):
        priorities[i].append(list(map(int, input().split())))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def update_smell():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            # 상어가 존재하는 해당위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], K]

def move():
    new_array = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if array[r][c] != 0:
                direction = directions[array[r][c] - 1] # 현재 상어 방향
                found = False

                for i in range(4):
                    nr = r + dr[priorities[array[r][c] -1][direction - 1][i] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][i] - 1]
                    if 0 <= nr < N and 0<= nc < N and smell[nr][nc][1] == 0:
                        directions[array[r][c] - 1] = priorities[array[r][c] -1][direction - 1][i]


                        if new_array[nr][nc] == 0:
                            new_array[nr][nc] = array[r][c]
                        else:
                            new_array[nr][nc] = min(new_array[nr][nc], array[r][c])
                        found = True
                        break
                if found:
                    continue

                # 자신의 냄새가 있는 곳으로 이동
                for i in range(4):
                    nr = r + dr[priorities[array[r][c] -1][direction - 1][i] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][i] - 1]
                    if 0 <= nr < N and 0 <= nc < N and smell[nr][nc][0] == array[r][c]:
                        directions[array[r][c] - 1] = priorities[array[r][c] -1][direction - 1][i]
                        new_array[nr][nc] = array[r][c]
                        break
    return new_array

time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    check = True
    for i in range(N):
        for j in range(N):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break
    if time >= 1000:
        print(-1)
        break




