# 그룹 조건
# 1. 일반 블록이 적어도 하나 있어야 한다 (전부 무지개 블록 x) (0)
# 2. 일반 블록의 색 모두 같아야 한다. (0)
# 3. 검은색 블록은 포함하면 안된다. (0)
# 4. 블록의 개수 >= 2 (0)
# 5. 기준 블록 존재: 무지개 블록이 아닌 블록, 행의 번호가 가장 작은 블록, 열번호가 가장 작은 블록

# 블록 그룹이 존재하는 동안 반복
# 크기가 가장 큰 블록 그룹
# 여러개라면 무지개 블록의 수가 가장 많은 그룹 -> 기준 블록의 행 번호가 가장 큰 -> 열번호가 가장 큰
# 블록 그룹의 블록 제거 -> 블록 그룹의 점수 제곱을 획득
# 90도 반시계 방향 회전
# 중력이 작용한다. : 블록이 행번호가 큰 쪽으로 떨어진다. (다른 블록이나 경계를 만날때 까지 이동한다.)

from collections import deque
from math import pow

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_group_list(graph):
    visited = [[False] * N for _ in range(N)]
    groups = []

    for r in range(N):
        for c in range(N):
            if graph[r][c] > 0 and not visited[r][c]:
                need_visit = deque([(r, c)])
                visited[r][c] = True
                rainbow_count, normal_count = 0, 1
                stand_r, stand_c = r, c
                stand_color = graph[r][c]
                tmp_group = {(r, c)}

                while need_visit:
                    row, column = need_visit.popleft()

                    for dr, dc in dir:
                        new_row, new_column = row + dr, column + dc

                        if new_row < 0 or new_row >= N or new_column < 0 or new_column >= N:
                            continue

                        # graph[r][c](stand_color) > 0이다.
                        if graph[new_row][new_column] == stand_color or graph[new_row][new_column] == 0:
                            if (new_row, new_column) not in tmp_group:  # 무지개 블록 방
                                if graph[new_row][new_column] > 0:
                                    visited[new_row][new_column] = True
                                    normal_count += 1
                                else:  ## 무지개 블럭
                                    rainbow_count += 1

                                tmp_group.add((new_row, new_column))
                                need_visit.append((new_row, new_column))

                if normal_count >= 1 and normal_count + rainbow_count >= 2:
                    groups.append((tmp_group, normal_count, rainbow_count, stand_r, stand_c))

    return groups


def rotate(graph):
    new_graph = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_graph[N - 1 - c][r] = graph[r][c]
    return new_graph


def move_down(graph):
    for c in range(N):
        for r in range(N - 2, -1, -1):
            if graph[r][c] >= 0:
                for i in range(r, N - 1):
                    if graph[i + 1][c] == -1:
                        break
                    if graph[i + 1][c] == -2:
                        graph[i][c], graph[i + 1][c] = graph[i + 1][c], graph[i][c]


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    group_lst = get_group_list(graph)
    if len(group_lst) == 0:
        break

    group_lst.sort(key=lambda x: ((x[1] + x[2]), x[2], x[3], x[4]), reverse=True)

    for r, c, in group_lst[0][0]:
        graph[r][c] = -2

    score = pow((group_lst[0][1] + group_lst[0][2]), 2)
    result += score

    ## 중력
    # -2 = 빈칸, -1 = 검은색, 0 = 무지개,
    move_down(graph)

    ## 90 반시계 회전
    graph = rotate(graph)

    # 중력
    move_down(graph)

print(int(result))
