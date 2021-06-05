N, n_cards = int(input()), set(map(int, input().split()))
M, m_cards = int(input()), list(map(int, input().split()))

for card in m_cards:
    if card in n_cards:
        print(1, end=" ")
    else:
        print(0, end=" ")

