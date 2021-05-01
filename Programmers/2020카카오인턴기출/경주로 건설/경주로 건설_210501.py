from collections import deque
import math

def bfs(board, r, c, d):
    # 0 == bottom, 1 == top, 2 == right, 3 == left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    N = len(board)
    need_visit = deque([(r, c, 0, d)])
    min_money = [[math.inf] * N for _ in range(N)]

    while need_visit:
        row, column, money, d = need_visit.popleft()

        for cur_d, (dr, dc) in enumerate(directions):
            new_r, new_c = row + dr, column + dc
            new_money = money + 100
            if d != cur_d:
                new_money += 500

            if new_r >= 0 and new_c >= 0 and new_r < N and new_c < N and board[new_r][new_c] != 1 and new_money < min_money[new_r][new_c]:
                min_money[new_r][new_c] = new_money
                need_visit.append((new_r, new_c, new_money, cur_d))

    return min_money[N - 1][N - 1]


def solution(board):
    answer = min(bfs(board, 0, 0, 0),bfs(board, 0, 0, 2))
    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))