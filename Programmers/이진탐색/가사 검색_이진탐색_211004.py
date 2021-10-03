from bisect import bisect_left, bisect_right
from collections import defaultdict


def count_between(arr, start, end):
    right_index = bisect_right(arr, end)
    left_index = bisect_left(arr, start)
    return right_index - left_index


def solution(words, queries):
    answer = []

    word_by_count = defaultdict(list)
    r_word_by_count = defaultdict(list)
    for word in words:
        n = len(word)
        word_by_count[n].append(word)
        r_word_by_count[n].append(word[::-1])

    for key in word_by_count.keys():
        word_by_count[key].sort()
    for key in r_word_by_count.keys():
        r_word_by_count[key].sort()



    for query in queries:
        nq = len(query)
        a_query = query.replace('?', 'a')
        z_query = query.replace('?', 'z')
        if query[0] == '?':
            res = count_between(r_word_by_count[nq], a_query[::-1], z_query[::-1])
        else:
            res = count_between(word_by_count[nq], a_query, z_query)
        answer.append(res)


    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

