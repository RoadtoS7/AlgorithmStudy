from collections import deque
from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
board = [input() for _ in range(R)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    result = 0
    q = deque([(x, y, board[x][y])])

    while q:
        r, c, path = q.pop()
        result = max(result, len(path))
        for dr, dc in direction:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r and 0 <= new_c and new_r < R and new_c < C and board[new_r][new_c] not in path:
                q.append((new_r, new_c, path + board[new_r][new_c]))
    return result

print(bfs(0, 0))

