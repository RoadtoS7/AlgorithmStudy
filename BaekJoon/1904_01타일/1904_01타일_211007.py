N = int(input())
dp = [0, 1, 2]

if N <= 2:
    print(dp[N])
else:
    for i in range(3, N + 1):
        r = dp[i - 1] + dp[i - 2]
        dp.append(r)

    print(dp[N])
