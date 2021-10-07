n = int(input())

last_num = 2
dp = [0, 1, 1]

if n > last_num:
    for i in range(last_num, n):
        res = dp[last_num] + dp[last_num - 1]
        dp.append(res)
        last_num += 1

print(dp[n])

