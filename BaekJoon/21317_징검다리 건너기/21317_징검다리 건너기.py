from sys import exit

N = int(input())
small, big = [0], [0]
for _ in range(N - 1):
    small_jump, big_jump = map(int, input().split())
    small.append(small_jump)
    big.append(big_jump)

K = int(input())

if N == 1:
    print(0)
    exit(0)

dp = [0] * (N + 1)
dp[2] = dp[1] + small[1]

if N == 2:
    print(dp[2])
    exit(0)

dp[3] = min(dp[2] + small[2], dp[1] + big[1])
if N == 3:
    print(dp[3])
    exit(0)


for i in range(4, N + 1):
    dp[i] = min(dp[i - 1] + small[i - 1],
                dp[i - 2] + big[i - 2])

print(dp[N])
