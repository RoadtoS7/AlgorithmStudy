N = int(input())

dp = [0] * (N + 1)
if N <= 3:
    if N % 2 == 0:
        print('CY')
    else:
        print('SK')
    exit(0)

dp[0], dp[1], dp[2], dp[3] = 0, 1, 0, 1

for i in range(4, N + 1):
    if min(dp[i - 3], dp[i - 1]) == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] == 1:
    print('SK')
else:
    print('CY')
