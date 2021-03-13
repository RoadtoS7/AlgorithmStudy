N = int(input())
words = [''] * N

for i in range(N):
    word = input()
    words[i] = (len(word), word)


words = list(set(words))
words.sort()
result = ""

print('\n'.join(map(lambda x: x[1], words)))

## 위의 과정을 아래와 같이 축소할 수 있다.
# 핵심: key에 lambda를 이용해서 인자를 넣는다.
words = list(set([input() for _ in range(int(input()))]))
words.sort(key=lambda x: (len(x), x))
print('\n'.join(words))
