def factorial(num):
    if top < num:
        for i in range(top + 1, num + 1):
            cache[i] = cache[i - 1] * i
        return cache[num]
    else:
        return cache[num]


T = int(input())
cache = [None] * 30
cache[0], cache[1] = 1, 1
top = 1

for _ in range(T):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial(N) * factorial(M - N))
    print(result)
