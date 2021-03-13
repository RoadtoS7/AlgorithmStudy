N = int(input())
words = [''] * N

for i in range(N):
    word = input()
    words[i] = (len(word), word)

words = list(set(words))
words.sort()
result = ""

print('\n'.join(map(lambda x: x[1], words)))
