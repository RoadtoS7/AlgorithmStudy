N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_card = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_card = cards[i] + cards[j] + cards[k]
            if sum_card > max_card and sum_card <= M:
                max_card = sum_card
print(max_card)
