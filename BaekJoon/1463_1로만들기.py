N = int(input())

cache = [0, 0, 1, 1]

if N <= 3:
    print(cache[N])
else:
    for i in range(4, N + 1):
        temp = cache[i - 1] + 1
        if i % 2 == 0:
            temp = min(temp, cache[i // 2] + 1)
        if i % 3 == 0:
            temp = min(temp, cache[i // 3] + 1)
        cache.append(temp)

    print(cache[N])