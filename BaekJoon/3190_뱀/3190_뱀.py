from collections import deque

N, K = int(input()), int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 2

d_count = int(input())
dir_change_lst = deque([])
for _ in range(d_count):
    time, direction = input().split()
    time = int(time)
    dir_change_lst.append((time, direction))

def turn_left(cur_dir, turn_direction):
    if turn_direction == 'L':
        return (cur_dir - 1) % 4
    else:
        return (cur_dir + 1) % 4



cur_dir = 0
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
total_time = 0
time, turning_direction = dir_change_lst.popleft()
r, c = 0, 0
snake = deque([(r, c)])

while True:
    if time == total_time:
        cur_dir = turn_left(cur_dir, turning_direction)
        if dir_change_lst:
            time, turning_direction = dir_change_lst.popleft()

    dr, dc = dir[cur_dir]
    r, c = r + dr, c + dc
    if r < 0 or r >= N or c < 0 or c >= N or graph[r][c] == 1:
        total_time += 1
        break

    snake.append((r, c))
    if graph[r][c] != 2:
        snaker, snakec = snake.popleft()
        graph[snaker][snakec] = 0
    graph[r][c] = 1
    total_time += 1

print(total_time)







