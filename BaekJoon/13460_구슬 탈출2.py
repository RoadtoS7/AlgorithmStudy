# 빨간 구슬과 파란 구슬은 같은 곳에 위치할 수 없다.
# 동시에 움직인다.
# 파란구슬이 빠지는 경우 (빨간 구슬은 빠지지 않고 파란 구슬만 빠지는 경우 or 빨간 구슬 빠지고 파란구슬도 빠지고)는 무조건 X
# 기울이는 동작을 그만하는 것: 더이상 구슬이 움직이지 않을 때까지
# 둘다 떨어지는 경우도 안된다.

from sys import stdin
from collections import deque

input = stdin.readline


def bfs(redr, redc, bluer, bluec):
    need_visit = deque([(redr, redc, bluer, bluec, 1)])
    visited = set()

    while need_visit:
        rr, rc, br, bc, count = need_visit.popleft()

        if count > 10:  ## 10을 초과하는 것이 등장하면, 이후로는 전부 10이상 걸린다.
            break

        for dr, dc in dir:
            new_red_r, new_red_c, new_blue_r, new_blue_c = rr, rc, br, bc
            rmovement, bmovement = 0, 0
            ## 변수의 선언 위치를 주의하자!!
            is_red_exit, is_blue_exit = False, False
            while graph[new_red_r + dr][new_red_c + dc] != '#':
                new_red_r += dr
                new_red_c += dc
                rmovement += 1

                if graph[new_red_r][new_red_c] == 'O':
                    is_red_exit = True
                    break

            while graph[new_blue_r + dr][new_blue_c + dc] != '#':
                new_blue_r += dr
                new_blue_c += dc
                bmovement += 1

                if graph[new_blue_r][new_blue_c] == 'O':
                    is_blue_exit = True
                    break

            # 파란색 구슬이 빠져나가면 빨간색 구슬이 빠져나갔는지 여부에 관계없이 -1이여야 한다.
            if is_blue_exit:
                continue

            if is_red_exit:
                return count

            if new_red_r == new_blue_r and new_red_c == new_blue_c:
                # 한칸 뒤로 이동하는 것 (앞으로 이동하는 것은 dr, dc를 더해줬으므로, 한칸 뒤로는 dr, dc를 빼주면된다!)
                if rmovement > bmovement:
                    new_red_r -= dr
                    new_red_c -= dc

                else:
                    new_blue_r -= dr
                    new_blue_c -= dc

            if (new_red_r, new_red_c, new_blue_r, new_blue_c) not in visited:
                need_visit.append((new_red_r, new_red_c, new_blue_r, new_blue_c, count + 1))
                visited.add((rr, rc, br, bc))

    return -1


N, M = map(int, input().split())
graph = []
redr, redc, bluer, bluec = 0, 0, 0, 0
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for r in range(N):
    row = list(input().rstrip())
    graph.append(row)
    for c in range(M):
        if row[c] == 'R':
            redr, redc = r, c

        if row[c] == 'B':
            bluer, bluec = r, c

graph[redr][redc] = '.'
graph[bluer][bluec] = '.'

print(bfs(redr, redc, bluer, bluec))
