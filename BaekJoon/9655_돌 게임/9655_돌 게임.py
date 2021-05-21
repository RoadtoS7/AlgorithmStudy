N = int(input())

dp = ['SK'] * N
turn_SK = True

if n == 1:
    n -= 1
if n == 3:
    n -= 3
if n == 2 or n == 4:
    print('')

def take(n, turn_SK):
    if n - 3 >= 0:
        if turn_SK:
            dp[n - 3] = 'SK'
        else:
            dp[n - 3] = 'CY'
        take(n - 3, not turn_SK)
    if n - 1 >= 0:
        if turn_SK:
            dp[n - 1] = 'SK'
        else:
            dp[n - 1] = 'CY'
        take(n - 1, not turn_SK)

take(N, turn_SK)
print(dp[0])
