# 상어: 자기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# 상어: 자신의 크기보다 작은 물고기만 먹을 수 있다. (크기 같은 물고기 먹을 수 없음)
# 상어: 크기가 같은 물고기는 먹을 수 없지만 지나갈 수 있디.
# 먹을 수 잇는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 여러마리라면, 거리가 가까운 고기글 먹으러 간다. (거리 = 지나가야 하는 칸의 최소값)
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기 (r값이 작은 물고기), 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다(c값이 작은 물고기).
# 1칸 이동시 1초 걸림
# 먹을 수 없는 물고기가 없을 때까지 몇초가 되는가?

# 마지막으로 상어를 먹었을 때의 시간을 저장해둔다.
# 처음 아기상어 크기 2

from collections import deque


def get_fish_distance(x, y, shark_size):
    ## x, y = 현재 shark의 위치
    # fish의 거리를 찾는다. -> fish의 사이즈와 함게 반환
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    need_visit = deque([(x, y)])
    fish_dist = list()  # (r, c, 거리, 사이즈)

    while need_visit:
        r, c = need_visit.popleft()

        for dr, dc in dir:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if dist[nr][nc] == -1 and graph[nr][nc] <= shark_size:
                dist[nr][nc] = dist[r][c] + 1
                need_visit.append((nr, nc))
                if 0 < graph[nr][nc] < 9:
                    fish_dist.append((nr, nc, dist[nr][nc], graph[nr][nc]))

    return fish_dist


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
time = 0
sharkr, sharkc = 0, 0
shark_size = 2
eat_count = 0

for r in range(N):
    for c in range(N):
        if graph[r][c] == 9:
            sharkr, sharkc = r, c
            graph[r][c] = 0

while True:
    fish_info = get_fish_distance(sharkr, sharkc, shark_size)
    if len(fish_info) == 0:
        break

    fish_info.sort(key=lambda x: (x[2], x[0], x[1], x[3]))

    is_available_fish = False
    for fish in fish_info:
        r, c, dist, size = fish

        if shark_size > size:
            is_available_fish = True
            sharkr, sharkc = r, c
            time += dist
            graph[r][c] = 0
            eat_count += 1

            if eat_count == shark_size:
                shark_size += 1
                eat_count = 0

            break

    if not is_available_fish:
        break

print(time)
