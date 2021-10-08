from itertools import combinations

L, C = map(int, input().split())
data = input().split()
bowls = {'a', 'e', 'i', 'o', 'u'}
answer = []
for word in list(combinations(data, L)):
    set_word = set(word)
    bowl_count = 0
    for bowl in bowls:
        if bowl in set_word:
            bowl_count += 1

    if bowl_count >= 1 and L - bowl_count >= 2:
        ans = ''.join(sorted(word))
        answer.append(ans)

[print(ans) for ans in sorted(answer)]

