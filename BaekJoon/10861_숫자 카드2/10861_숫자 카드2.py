from collections import defaultdict

N, cards = int(input()), list(map(int, input().split()))
M, targets = int(input()), list(map(int, input().split()))

count = defaultdict(int)
for card in cards:
    count[card] += 1

result = []
for target in targets:
    if target in count:
        result.append(str(count[target]))
    else:
        result.append('0')

print(" ".join(result))

