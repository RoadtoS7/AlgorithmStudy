T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    multi_M = 1
    for i in range(N):
        multi_M *= (M - i)

    multi_N = 1
    for j in range(2, N + 1):
        multi_N *= j

    print(multi_M // multi_N)
