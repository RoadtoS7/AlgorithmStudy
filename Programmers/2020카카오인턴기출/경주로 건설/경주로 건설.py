from collections import deque
import math


def bfs(r, c, board, N, head):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    min_table = [[math.inf] * N for _ in range(N)]
    lst = [(r, c), 0, head]
    need_visit = deque([lst])
    result = []

    while need_visit:
        (row, column), money, head = need_visit.popleft()

        if row == N - 1 and column == N - 1:
            result.append(money)
            continue
        #  bottom = 0, top = 1, right = 2, left = 3
        for cur_dir, (dr, dc) in enumerate(directions):
            new_r, new_c = row + dr, column + dc
            cur_money = money + 100 if head == cur_dir else money + 600

            ## 무한루프에 빠지지 않는 방법: 현재 위치에서의 금액이 min_table에 저장된 값보다 작을때 에만 다음 위치로 넘어갈 수 있다.
            if new_r >= 0 and new_c >= 0 and new_r < N and new_c < N and board[new_r][new_c] == 0 and cur_money < min_table[new_r][new_c]:
                min_table[new_r][new_c] = cur_money
                new_location = [(new_r, new_c), cur_money, cur_dir]
                need_visit.append(new_location)

    return min_table[-1][-1]


def solution(board):
    answer = min(bfs(0, 0, board, len(board), 0), bfs(0, 0, board, len(board), 2))
    return answer


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
