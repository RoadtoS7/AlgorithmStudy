from bisect import bisect_left, bisect_right


def count_by_range(lst, start, end):
    left_index = bisect_left(lst, start)
    right_index = bisect_right(lst, end)
    return right_index - left_index


## 길이별 단어 리스트
word_by_length = [[] for _ in range(10001)]
# 길이별로 단어를 뒤집어서 저장하기 위한 리스트
reversed_words = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    for word in words:
        n = len(word)
        word_by_length[n].append(word)
        reversed_words[n].append(word[::-1])

    for i in range(10001):
        word_by_length[i].sort()
        reversed_words[i].sort()

    for q in queries:
        q_len = len(q)
        start = q.replace('?', 'a')
        end = q.replace('?', 'z')
        if q[0] != '?':
            result = count_by_range(word_by_length[q_len], start, end)
        else:
            result = count_by_range(reversed_words[q_len], start[::-1], end[::-1])
        answer.append(result)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))