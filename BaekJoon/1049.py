N, M = map(int, input().split())

minPackPrice = 1001
minEachPrice = 1001
for i in range(M):
    packPrice, eachPrice = map(int, input().split())
    if packPrice < minPackPrice:
        minPackPrice = packPrice
    if eachPrice < minEachPrice:
        minEachPrice = eachPrice

if minEachPrice * 6 < minPackPrice:
    print(minEachPrice * N)
else:
    eachCount = N % 6
    if eachCount * minEachPrice < minPackPrice:
        print(minPackPrice * (N // 6) + minEachPrice * eachCount)
    else:
        print(minPackPrice * (N // 6) + minPackPrice)