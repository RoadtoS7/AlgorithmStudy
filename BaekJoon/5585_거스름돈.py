money = int(input())
money = 1000 - money
cash = [500, 100, 50, 10, 5, 1]

result = 0
for i in cash:
    result += (money // i)
    money = money % i

print(result)
