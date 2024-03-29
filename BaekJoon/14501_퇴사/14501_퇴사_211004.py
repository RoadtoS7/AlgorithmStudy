N = int(input())
T, P = [], []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N + 1)
max_value = -1

for i in range(N -1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(dp[i + T[i]] + P[i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(dp)
