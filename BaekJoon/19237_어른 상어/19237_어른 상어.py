from collections import deque
from bisect import insort
import sys


def move_shark(sharkid, r, c, sharkdir):
    same_perfume_loc = deque([])

    for d in dir[sharkid][sharkdir]:
        newr, newc = r + dr[d], c + dc[d]
        if 0 <= newr < N and 0 <= newc < N:
            if perfume[newr][newc] is None:
                shark[sharkid] = [newr, newc, d]
                graph[r][c].remove(sharkid)
                if len(graph[newr][newc]) == 0:
                    graph[newr][newc] = [sharkid]
                else:
                    insort(graph[newr][newc], sharkid)

                return

            if perfume[newr][newc][0] == sharkid:
                same_perfume_loc.append((newr, newc, d))

    if same_perfume_loc:
        r, c, d = same_perfume_loc.popleft()
        shark[sharkid] = [r, c, d]
        insort(graph[r][c], sharkid)


def remove_shark():
    for r in range(N):
        for c in range(N):
            while len(graph[r][c]) >= 2:
                sharkid = graph[r][c].pop()
                del shark[sharkid]


def decrease_perfume():
    for r in range(N):
        for c in range(N):
            if perfume[r][c] is not None:
                perfume[r][c][1] -= 1
                if perfume[r][c][1] == 0:
                    perfume[r][c] = None

def add_perfume(sharkid, sharkr, sharkc):
    perfume[sharkr][sharkc] = [sharkid, K]



N, M, K = map(int, input().split())
graph = [list( map(int, input().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        if graph[r][c] == 0:
            graph[r][c] = []
        else:
            graph[r][c] = [graph[r][c]]


perfume = [[None] * N for _ in range(N)]
shark = dict()
dir = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
time = 0

# 상어 위치 구하기
for r in range(N):
    for c in range(N):
        if len(graph[r][c]) >= 1:
            graph[r][c][0] -= 1
            shark[graph[r][c][0]] = [r, c]
            perfume[r][c] = [graph[r][c][0], M]

# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
for i, sharkdir in enumerate(map(int, input().split())):
    shark[i].append(sharkdir - 1)

# 상어 방향 우선순위
for _ in range(M):
    tmp = []
    for _ in range(4):
        dirlist = list(map(int, input().split()))
        for i in range(4):
            dirlist[i] -= 1
        tmp.append(dirlist)
    dir.append(tmp)

while len(shark) > 1:
    if time > 1000:
        print(-1)
        sys.exit(0)

    for sharkid, (sharkr, sharkc, sharkdir) in shark.items():
        move_shark(sharkid, sharkr, sharkc, sharkdir)


    remove_shark()
    decrease_perfume()

    for sharkid, (sharkr, sharkc, _) in shark.items():
        add_perfume(sharkid, sharkr, sharkc)
    time += 1



print(time)





