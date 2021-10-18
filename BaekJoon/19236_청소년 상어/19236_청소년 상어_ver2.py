from copy import deepcopy

def turn_left(direction):
    return (direction + 1) % 8


# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish_location(array, fish_id):
    for r in range(4):
        for c in range(4):
            if array[r][c][0] == fish_id:
                return (r, c)
    return None

# 물고기를 회전 및 이동시키는 함수
def move_all_fish(array, sharkr, sharkc):
    for i in range(1, 17):
        position = find_fish_location(array, i)
        if position == None:
            continue

        fishr, fishc = position
        direction = array[fishr][fishc][1]

        # 현재 방향으로 이동가능한지 확인
        for j in range(8):
            nr, nc = fishr + dr[direction], fishc + dc[direction]

            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                direction = turn_left(direction)
                continue

            if nr == sharkr and nc == sharkc:
                direction = turn_left(direction)
                continue

            array[fishr][fishc][1] = direction
            array[nr][nc], array[fishr][fishc] = array[fishr][fishc], array[nr][nc]

# 상어가 현재 먹을 수 있는 물고기들의 위치 반환
def get_available_fish_location(array, sharkr, sharkc):
    fish_lst = []
    direction = array[sharkr][sharkc][1]

    for i in range(4):
        sharkr += dr[direction]
        sharkc += dr[direction]


        if 0 <= sharkr < 4 and 0 <= sharkc <4:
            if array[sharkr][sharkc][0] != -1:
                fish_lst.append((sharkr, sharkc))

    return fish_lst

def dfs(array, sharkr, sharkc, count):
    global max_fish_count
    array = deepcopy(array)

    # 현재 위치의 물고기 먹음
    count += array[sharkr][sharkc][0]
    array[sharkr][sharkc][0] = -1

    move_all_fish(array, sharkr, sharkc)

    # 상어가 먹을 수 있는 물고기 계산
    fish_lst = get_available_fish_location(array, sharkr, sharkc)
    if len(fish_lst) == 0:
        max_fish_count = max(max_fish_count, count)
        return
    for fishr, fishc in fish_lst:
        dfs(array, fishr, fishc, count)

# 8가지 방향 정의
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
array = [[None] * 4 for _ in range(4)]
max_fish_count = 0

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        ## 각 위치마다 물고기 번호, 방향 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dfs(array, 0, 0, 0)
print(max_fish_count)
