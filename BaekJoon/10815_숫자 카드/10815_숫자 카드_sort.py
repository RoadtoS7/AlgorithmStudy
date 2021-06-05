N, n_cards = int(input()), list(map(int, input().split()))
M, m_cards = int(input()), list(map(int, input().split()))

is_exist = {card: 0 for card in m_cards}
n_cards.sort()
m_cards.sort()

n, m = 0, 0
while m < M:
    if n_cards[n] == m_cards[m]:
        is_exist[m_cards[m]] = 1
        if n > N:
            n += 1
        m += 1
        continue
    elif n_cards[n] < m_cards[m]:
        if n < N:
            n += 1
        continue
    else:
        is_exist[m_cards[m]] = 0
        m += 1
        continue

for value in is_exist.values():
    print(value, end=" ")




