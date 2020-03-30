coin = (500, 100, 50, 10, 5, 1)

won = 1000-int(input())
result = 0
for i in range(len(coin)):
    result += won // coin[i]
    won = won % coin[i]

print(result)