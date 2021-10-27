# 초록색 보드 = 행이 꽉찬 경우 (0, 1)행에 블록 들어있는 경우
# 블루 = 열이 꽉찬 경우 (0, 1) 열에 블록 들어있는 경우

blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

def put_green_block(type, r, c):
    # 1 집어 넣기
    if type == 1 or type == 3:
        green[1][c] = 1
        last_r = 1
        for r in range(1, 5):
            if green[r + 1][c] == 0:
                green[r + 1][c], green[r][c] = green[r][c], green[r + 1][c]
                last_r = r + 1
            else:
                break

        if type == 3:
            green[last_r - 1][c] = 1

    if type == 2:
        green[1][c], green[1][c + 1] = 1, 1
        for r in range(1, 5):
            if green[r + 1][c] == 0 and green[r + 1][c + 1] == 0:
                green[r + 1][c], green[r][c] = green[r][c], green[r + 1][c]
                green[r + 1][c + 1], green[r][c + 1] = green[r][c + 1], green[r + 1][c + 1]
            else:
                break



def get_green_score(green):
    count = 0
    for r in range(6):
        if sum(green[r]) == 4:
            count += 1

            for c in range(4):
                green[r][c] = 0

    return count


def move_down_green(green, count):
    if count == 0:
        return

    for c in range(4):
        for r in range(5, -1, -1):
            if green[r][c] == 1:
                for i in range(r, 5):
                    if green[r + 1][c] == 0:
                        green[r][c], green[r + 1][c] = green[r + 1][c], green[r][c]


def get_green_zeroone(green):
    is_zero, is_one = False, False
    for c in range(4):
        is_zero = green[0][c] > 0
        if is_zero:
            break

    for c in range(4):
        is_one = green[1][c] > 0
        if is_one:
            break


    res = 0
    if is_zero: res += 1
    if is_one: res += 1
    return res

def move_down_green_count(green, count):
    if count == 0:
        return

    for i in range(count):
        for c in range(4):
            green[5 - i][c] = 0

    for c in range(4):
        for r in range(5, 0, -1):
            green[r][c], green[r - 1][c] = green[r - 1][c], green[r][c]

def get_blue_score(blue):
    count = 0

    for c in range(5, -1, -1):
        sum_col = 0
        for r in range(4):
            sum_col += blue[r][c]

        if sum_col == 4:
            count += 1
            for r in range(4):
                blue[c][r] = 0
    return count

def move_blue_right(blue, score):
    if score == 0:
        return
    for r in range(4):
        for c in range(5, -1, -1):
            if blue[r][c] == 0:
                continue

            for i in range(c, 5):
                if blue[r][i + 1] == 0:
                    blue[r][i], blue[r][i + 1] = blue[r][i + 1], blue[r][i]


def put_blue_block(type, r, c):
    if type == 1 or type == 2:
        blue[r][1] = 1
        last_c = 1

        for c in range(1, 5):
            if blue[r][c + 1] == 0:
                blue[r][c], blue[r][c + 1] = blue[r][c + 1], blue[r][c]
                last_c = c + 1
            else:
                break

        if type == 2:
            blue[r][last_c - 1] = 1

    if type == 3:
        blue[r][1], blue[r + 1][1] = 1, 1
        for c in range(1, 5):
            if blue[r][c + 1] == 0 and blue[r + 1][c + 1] == 0:
                blue[r][c], blue[r][c + 1] = blue[r][c + 1], blue[r][c]
                blue[r + 1][c], blue[r + 1][c + 1] = blue[r + 1][c + 1], blue[r + 1][c]
            else:
                break


def check_blue_zeroone(blue):
    is_zero, is_one = False, False
    for r in range(4):
        if blue[r][0] > 0:
            is_zero = True
        if blue[r][1] > 0:
            is_one = True

    res = 0
    if is_zero: res += 1
    if is_one: res += 1
    return res


def move_right_blue_count(blue, count):
    if count == 0:
        return
    for r in range(4):
        for c in range(count):
            blue[r][5 - c] = 0

    for r in range(4):
        for c in range(5, 0, -1):
            blue[r][c], blue[r][c - 1] = blue[r][c - 1], blue[r][c]


N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
score = 0


for type, r, c in blocks:

    put_green_block(type, r, c) #

    count = get_green_score(green) #
    score += count #
    move_down_green(green, count) #

    cnt = get_green_zeroone(green)
    move_down_green_count(green, cnt)


    put_blue_block(type, r, c) #
    count = get_blue_score(blue)
    score += count
    move_blue_right(blue, count)

    cnt = check_blue_zeroone(blue)
    move_right_blue_count(blue, cnt)


block_count = sum(sum(i) for i in blue) + sum(sum(j) for j in green)
print(score)
print(block_count)



'''green test'''
# put_green_block(1, 1, 1)
# put_green_block(2, 3, 0)
# put_green_block(2, 2, 2)
# put_green_block(2, 3, 2)
# get_green_score(green)
# put_green_block(3, 1, 3)
# put_green_block(2, 0, 0)
# put_green_block(3, 2, 0)
# put_green_block(3, 1, 2)
# get_green_score(green)
# move_down_green(green)

# put_blue_block(1, 1, 1)
# put_blue_block(2, 3, 0)
# put_blue_block(3, 2, 2)
# put_blue_block(3, 2, 3)
# put_blue_block(3, 1, 3)
# count = check_blue_zeroone(blue)
# move_right_blue_count(blue, count)
# put_blue_block(2, 0, 0)
# put_blue_block(3, 2, 0)
# count = check_blue_zeroone(blue)
# move_right_blue_count(blue, count)
# put_blue_block(3, 1, 2)
# count = check_blue_zeroone(blue)
# move_right_blue_count(blue, count)
