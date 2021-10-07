N = int(input())

count5 = N // 5
count3 = (N - count5*5) // 3

while count5 >= 0 and 5 * count5 + count3 * 3 != N:
    count5 -= 1
    count3 = (N - count5*5) // 3

if count5 < 0:
    print(-1)
else:
    print(count5 + count3)

