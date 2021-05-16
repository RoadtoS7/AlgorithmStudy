from sys import stdin
input = stdin.readline

def dfs(index, count):
    global max_count
    if count == K - 5:
        readable_count = 0
        for word in words:
            for letter in word:
                if not is_readable_alphabet[ord(letter) - ord('a')]:
                    break
            else:
                readable_count += 1

        max_count = max(readable_count, max_count)
        return

    for i in range(index, 26):
        if not is_readable_alphabet[i]:
            is_readable_alphabet[i] = True
            dfs(index + 1, count + 1)
            is_readable_alphabet[i] = False




N, K = map(int, input().split())

if K < 5 or K == 26:
    print(0 if K != 26 else N )
    exit(0)

words = [set(input().lstrip('anta').rstrip('tica\n')) for _ in range(N)]
is_readable_alphabet = [False] * 26
max_count = -1

for a in ('a', 'n', 't', 'i', 'c'):
    is_readable_alphabet[ord(a) - ord('a')] = True

dfs(0, 0)
print(max_count)

