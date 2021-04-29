from collections import defaultdict


def solution(gems):
    gem_set_length = len(set(gems))
    N = len(gems)

    if gem_set_length == N:
        return [1, N]
    if gem_set_length == 1:
        return [1, 1]

    i, j, min_length = 0, gem_set_length - 1, N + 1

    exist_gems = defaultdict(int)
    for k in range(i, j + 1):
        exist_gems[gems[k]] += 1

    answer = []
    # 오른쪽이 끝까지 갔을 때에도 모든 보석이 존재하지 않는다면, 조건을 만족할 수 없다는 것이므로 줄인다.
    while i < N and j < N:
        if len(exist_gems) == gem_set_length:
            if min_length > j - i:
                min_length = j - i
                answer = [i + 1, j + 1]

            exist_gems[gems[i]] -= 1
            if exist_gems[gems[i]] == 0:
                del exist_gems[gems[i]]
            i += 1

        else:
            j += 1
            if j < N:
                exist_gems[gems[j]] += 1


    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
