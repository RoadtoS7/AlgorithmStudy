N = int(input())

numbers = [1 for _ in range(N)]

i2, i3, i5 = 0, 0, 0
ugly2, ugly3, ugly5 = 2, 3, 5
for l in range(1, N):
    m = min(ugly2, ugly3, ugly5)
    numbers[l] = m

    if ugly2 == m:
        i2 += 1
        ugly2 = numbers[i2] * 2
    if ugly3 == m:
        i3 += 1
        ugly3 = numbers[i3] * 3
    if ugly5 == m:
        i5 += 1
        ugly5 = numbers[i5] * 5

print(numbers[-1])


