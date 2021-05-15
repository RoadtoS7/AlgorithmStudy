from sys import stdin
input = stdin.readline
words, bomb = list(input().strip()), list(input().strip())

b_len = len(bomb)
i = 0
count = 0
while i < len(words):
    if words[i:i + b_len] == bomb:
        words = words[:i] + words[i+b_len:]

        if i >= b_len:
            i -= b_len
        else:
            i = 0
        continue
    i += 1

if words:
    print(words)
else:
    print('FRULA')


