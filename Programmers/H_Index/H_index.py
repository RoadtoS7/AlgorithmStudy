def solution(citations):
    n = len(citations)
    answer = n
    citations.sort(reverse=True)

    for i in range(n):
        while answer > citations[i]:
            if answer <= i:
                break
            answer -= 1
    return answer