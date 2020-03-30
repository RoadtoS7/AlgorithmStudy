a, b = input().split()

minimum = 1000000000000000000000000000000000
cha = len(b) - len(a)
if cha == 0:
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1


else:
    for i in range(cha + 1):
        result = 0

        for k in range(i, len(b)-(cha-i)-1):
            if a[k-i] != b[k]:
                result += 1
        if minimum >= result:
            minimum = result

print(minimum)
