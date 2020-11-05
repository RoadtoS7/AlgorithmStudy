def solution(s):
    answer = []
    answer = cycle(s, [0, 0])
    return answer

def cycle(x, result):
    x_0 = 0
    x_1 = 0
    for text in x:
        if text == '0':
            x_0 += 1
        else:
            x_1 += 1

    result[1] += x_0
    next_x = format(x_1, 'b')
    result[0] += 1
    if next_x == "1":
        return result
    else:
        return cycle(next_x, result)

