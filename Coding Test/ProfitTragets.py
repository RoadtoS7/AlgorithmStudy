# 재무 분석가는 집합으로 대표되는 수익성 있는 주식 포트폴리오를 책임진다.
# 배열의 각 항목은 해당 주식의 연간 이익을 나타낸다.
# 분석가는 목표 이익에 도달한 모든 뚜렷한 쌍의 주식을 모은다.

def stockPairs(stocksProfit, target):
    used = []
    count = 0
    for profit in stocksProfit:
        find = target - profit
        if find in stocksProfit and not(find in used):
            count += 1
            used.append(find)
            used.append(target)
    print(count)

stockPairs([1, 3, 46, 1, 3, 9] ,47)
