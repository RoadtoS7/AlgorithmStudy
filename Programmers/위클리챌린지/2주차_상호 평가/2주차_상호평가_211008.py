def get_grade(s):
    if s >= 90:
        return'A'
    elif s >= 80:
        return 'B'
    elif s >= 70:
        return 'C'
    elif s >= 50:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    count = len(scores)
    for j in range(count):
        res = 0
        maxs, mins = -1, 1e9
        num = count
        for i in range(count):
            maxs = max(maxs, scores[j][i])
            mins = min(mins, scores[i][j])
            res += scores[i][j]

        if scores[j][j] == maxs or scores[j][j] == mins:
            num -= 1
            res -= scores[j][j]

        mean = res / num
        answer += get_grade(mean)

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))