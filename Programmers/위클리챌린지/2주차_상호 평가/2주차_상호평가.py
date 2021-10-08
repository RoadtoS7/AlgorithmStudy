from collections import Counter

def get_grade(score):
    if score < 50:
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

def solution(scores):
    answer = ''
    n = len(scores)

    for j in range(n):
        min_s, max_s, total = 1e9, -1, 0
        col = []
        l = n

        for i in range(n):
            min_s = min(min_s, scores[i][j])
            max_s = max(max_s, scores[i][j])
            total += scores[i][j]
            col.append(scores[i][j])

        counter = Counter(col)

        if scores[j][j] == min_s or scores[j][j] == max_s:
            if counter[scores[j][j]] == 1:
                total -= scores[j][j]
                l -= 1

        mean = total / l
        answer += get_grade(mean)

    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))