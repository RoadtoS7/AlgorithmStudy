T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [[0] * M for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    for i, number in enumerate(numbers):
        mok, namujee = i // M, i % M
        graph[mok][namujee] = number

    for i in range(N):
        dp[i][0] = graph[i][0]

    for j in range(1, M):
        for i in range(N):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            if i == N - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]

            dp[i][j] = max(left, left_up, left_down) + graph[i][j]

    result = 0
    for i in range(N):
        result = max(result, dp[i][-1])
    print(result)





