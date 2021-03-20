def solution(people, limit):
    people.sort()
    i, j, answer = 0, len(people) - 1, 0
    while i <= j :
        if people[j] < limit:
            if people[j] + people[i] <= limit:
                answer += 1
                i += 1
                j -= 1
                continue

        answer += 1
        j -= 1

    return answer

people = list(map(int, input().split(',')))
limit = int(input())
answer = solution(people, limit)
print(answer)