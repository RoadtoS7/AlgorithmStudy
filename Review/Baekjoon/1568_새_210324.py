N = int(input())

K, count = 1, 0
while N > 0:
    if N < K:
        K = 1
    N -= K
    K += 1
    count += 1
print(count)
