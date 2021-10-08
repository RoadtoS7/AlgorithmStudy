from collections import Counter, defaultdict

T = int(input())
words = [input() for _ in range(T)]

def is_sudo(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False

        left += 1
        right -= 1
    return True

def check(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            res1 = is_sudo(word, left + 1, right)
            res2 = is_sudo(word, left, right -1)
            if res1 or res2:
                return 1
            else:
                return 2

    return 0

for word in words:
    res = check(word)
    print(res)







