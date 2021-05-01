def solution(board, moves):
    basket = []
    answer = 0

    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] != 0:
                basket.append(board[j][move - 1])
                board[j][move - 1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        answer += 2
                        basket.pop()
                        basket.pop()
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))