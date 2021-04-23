N, A = int(input()), list(map(int, input().split()))
cache = [0] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and cache[i] < cache[j]:
            cache[i] = cache[j]
    cache[i] += 1

print(max(cache))
