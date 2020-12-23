import heapq

n = int(input())
numbers = []
result = []
for _ in range(n):
    data = int(input())
    if data == 0:
        if numbers:
            result.append(heapq.heappop(numbers))
        else:
            result.append(0)
    else:
        heapq.heappush(numbers, data)

for item in result:
    print(item)
