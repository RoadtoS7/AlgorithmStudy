from collections import defaultdict


def solution(gems):
    gem_set = set(gems)
    gem_set_length = len(gem_set)
    N = len(gems)

    if gem_set_length == 1:
        return [1, 1]
    if gem_set_length == N:
        return [1, N]

    i, j, min_length = 0, gem_set_length - 1, N + 1
    result = []
    exist_gems = defaultdict(int)

    for k in range(i, j + 1):
        exist_gems[gems[k]] += 1

    while i < N and j < N:
        if len(exist_gems) == gem_set_length:
            if min_length > j - i:
                min_length = j - i
                result = [i + 1, j + 1]

            exist_gems[gems[i]] -= 1
            if exist_gems[gems[i]] == 0:
                del exist_gems[gems[i]]

            i += 1

        else:
            j += 1
            if j < N:
                exist_gems[gems[j]] += 1

    return result


print(solution(["AA", "AB", "AC", "AA", "AC"]))
