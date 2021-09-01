from collections import Counter

N, cards = int(input()), list(map(int, input().split()))
M, targets = int(input()), list(map(int, input().split()))

card_count = Counter(cards)
cards.sort()
result = []
for target in targets:
    start, end = 0, N - 1
    is_exist = False
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] > target:
            start = mid + 1
        elif cards[mid] < target:
            end = mid - 1
        else:
            result.append(str(card_count[target]))
            is_exist = True
            break

    if not is_exist:
        result.append('0')

print(" ".join(result))
