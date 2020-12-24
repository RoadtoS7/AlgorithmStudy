import heapq

card_group = list()
n = int(input())

for _ in range(n):
    heapq.heappush(card_group, int(input()))

result = 0
while len(card_group) != 1:
    first_card_group = heapq.heappop(card_group)
    second_card_group = heapq.heappop(card_group)
    result += second_card_group + first_card_group
    heapq.heappush(card_group, second_card_group + first_card_group)

print(result)