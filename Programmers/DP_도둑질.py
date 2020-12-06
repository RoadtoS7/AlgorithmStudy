def solution(money):
    robbed_money1 = [0] * len(money)
    robbed_money1[0] = money[0]
    robbed_money1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        robbed_money1[i] = max(robbed_money1[i-1], money[i] + robbed_money1[i-2])

    robbed_money2 = [0] * len(money)
    robbed_money2[0] = 0
    robbed_money2[1] = money[1]

    for i in range(2, len(money)):
        robbed_money2[i] = max(robbed_money2[i-1], money[i] + robbed_money2[i-2])

    return max(robbed_money2[-1], robbed_money1[-2])