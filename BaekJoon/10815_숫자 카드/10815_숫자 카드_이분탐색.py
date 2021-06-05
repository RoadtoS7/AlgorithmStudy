from sys import stdin

input = stdin.readline
N, n_cards = int(input()), list(map(int, input().split()))
M, m_cards = int(input()), list(map(int, input().split()))

n_cards.sort()

for card in m_cards:
    end_flag = False
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2

        if card > n_cards[mid]:
            start = mid + 1
        elif card < n_cards[mid]:
            end = mid - 1
        else:
            print(1, end=" ")
            end_flag = True
            break
    if not end_flag:
        print(0, end=" ")
