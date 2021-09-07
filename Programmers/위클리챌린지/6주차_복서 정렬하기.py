def solution(weights, head2head):
    n = len(weights)
    answer, win_rate, bigger_win_count = [], [], []

    for i in range(n):
        win_count, big_win_count, game_count = 0, 0, 0
        for j in range(n):
            if i != j and head2head[i][j] == 'W':
                win_count += 1
                if weights[i] < weights[j]:
                    big_win_count += 1
            if head2head[i][j] != 'N':
                game_count += 1

        game_rate = 0
        if game_count != 0:
            game_rate = win_count / game_count

        win_rate.append(game_rate)
        bigger_win_count.append(big_win_count)

    answer = sorted(list(range(1, n + 1)), key=lambda x: (-win_rate[x - 1], -bigger_win_count[x - 1], -weights[x - 1], x))
    return answer
