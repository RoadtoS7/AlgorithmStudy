import heapq
n, m = map(int, input().split())
numbers = list()
numbers.append(0)
for i in range(1, n + 1):
    heapq.heappush(numbers, i)

info = list()
for _ in range(m):
    before, after = map(int, input().split())
    info.append((before, after))

for before, after in info:
    numbers[before], numbers[after] = numbers[after], numbers[before]

result = ""
for i in range(1, len(numbers)):
    result += str(numbers[i]) + " "
print(result)


