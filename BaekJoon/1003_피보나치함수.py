T = int(input())

counts = [0] * 41
counts[0], counts[1] = (1, 0), (0, 1)
top = 1

for _ in range(T):
    N = int(input())
    if N <= top:
        print(counts[N][0], counts[N][1], end=' ')

    else:
        for i in range(top + 1, N + 1):
            counts[i] = (counts[i - 1][0] + counts[i - 2][0], counts[i - 1][1] + counts[i - 2][1])

        top = N
        print(counts[N][0], counts[N][1], end=' ')
