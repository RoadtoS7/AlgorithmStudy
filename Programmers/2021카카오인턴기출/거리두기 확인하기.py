def solution(places):
    answer = []

    def is_not_safe_dir_two(place, r, c, dr, dc):
        new_r, new_c = r, c
        if dr == 0 and dc == 1:
            new_c = c + 1
        elif dr == 0 and dc == -1:
            new_c = c - 1
        elif dr == 1 and dc == 0:
            new_r = r + 1
        elif dr == -1 and dc == 0:
            new_r = r - 1

        if 0 <= new_r < 5 and 0 <= new_c < 5:
            if place[new_r][new_c] == 'P':
                return True
        return False

    def is_not_safe_cross(place, r, c):
        dir_cross = [(-1, +1), (+1, +1), (-1, -1), (+1, -1)]
        for dr, dc in dir_cross:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 5 and 0 <= new_c < 5 and place[new_r][new_c] == 'P':
                if place[new_r][c] != 'X' or place[r][new_c] != 'X':
                    return True

        return False

    def is_not_safe_dir(place, r, c):
        dir_one = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in dir_one:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 5 and 0 <= new_c < 5:
                if place[new_r][new_c] == 'P':
                    return True
                elif place[new_r][new_c] == 'O' and is_not_safe_dir_two(place, new_r, new_c, dr, dc):
                    return True
        return False

    def check_place(place):
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    if is_not_safe_dir(place, r, c):
                        return False
                    elif is_not_safe_cross(place, r, c):
                        return False

        return True

    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
