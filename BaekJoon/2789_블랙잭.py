from sys import stdin
n, m = map(int, stdin.readline().split())
data = list(map(int, stdin.readline().split()))

result = 0
length = len(data)
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = data[i] + data[j] + data[k]
            if sum <= m:
                result = max(result, sum)
print(result)