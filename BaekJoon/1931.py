num = int(input())
c = list()
for i in range(0, num):
        a,b = input().split()
        c.append((a,b))

d = sorted(c, key=lambda x: x[1])
print(d)

