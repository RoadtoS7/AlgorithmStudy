from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())

graph = [input() for _ in range(R)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
x, y, count = 0, 0, 0


def bfs(x, y):
    global count
    q = deque([(x, y, graph[x][y])])

    while q:
        x, y, path = q.pop()
        count = max(count, len(path))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < R and ny < C and graph[nx][ny] not in path:
                q.append((nx, ny, path + graph[nx][ny]))

bfs(0, 0)
print(count)
