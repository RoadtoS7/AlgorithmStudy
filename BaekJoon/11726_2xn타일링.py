n = int(input())
cache = [0] * 1001
cache[1], cache[2] = 1, 2

for i in range(3, n + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[n] % 10007)
