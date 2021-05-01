def solution(board, moves):
    top_row = [-1] * len(board)
    basket = []
    answer = 0

    for c in range(len(board)):
        for r in range(len(board) - 1, -1, -1):
            if board[r][c] != 0:
                top_row[c] = r

    for move in moves:
        c = move -1
        if top_row[c] != len(board):
            if not basket:
                basket.append(board[top_row[c]][c])
                top_row[c] += 1
                continue

            if basket[-1] == board[top_row[c]][c]:
                answer += 2
                basket.pop()
                top_row[c] += 1
            else:
                basket.append(board[top_row[c]][c])
                top_row[c] += 1

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))