import heapq

N, M = map(int, input().split())
books = list(map(int, input().split()))

largest = max(max(books), -min(books))

positive = []
negative = []
for book in books:
    if book > 0:
        heapq.heappush(positive, -book)
    else:
        heapq.heappush(negative, book)

result = 0
while positive:
    result += heapq.heappop(positive)
    for _ in range(M - 1):
        if positive:
            heapq.heappop(positive)

while negative:
    result += heapq.heappop(negative)
    for _ in range(M - 1):
        if negative:
            heapq.heappop(negative)

print(-2 * result - largest)

