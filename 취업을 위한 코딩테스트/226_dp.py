N, M = map(int, input().split())
moneys = [int(input()) for _ in range(N)]
dp = [1e9 for _ in range(M + 1)]
dp[0] = 0

for money in moneys:
    for i in range(money, M + 1):
        dp[i] = min(dp[i], dp[i - money] + 1)

if dp[M] == 1e9:
    print(-1)
else:
    print(dp[M])
