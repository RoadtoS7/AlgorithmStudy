import sys
input = sys.stdin.readline
n = int(input())

array = []
for _ in range(n):
    deadline, count = map(int, input().split())
    array.append((deadline, count))

array.sort(key=lambda x: (x[0], -x[1] ))

time = 0
result = 0
for deadline, count in array:
    if time < deadline:
        time += 1
        result += count

print(result)

