count = int(input())

a = list(map(int,input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

result = 0
for i in range(count):
    result += a[i]*b[i]

print(result)
