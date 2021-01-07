# 양수와 음수를 나눠서 생각할 것!
# m 권씩 묶었을 때 가장 먼 곳에 있는 책까지 가야 한다.
# 가장 긴거를 한번만 가는 것이 낫다. = 마지막에 가야한다.
# 짧은 것부터 -> 큰 순으로 가는 것이 나을 듯
# 양수쪽에 갔을 때 양수쪽의 일을 다 하고 오는 것이 낫다.(음수쪽에 갔을 때 음수쪽의 책을 모두 배달하고 오는 것이 낫다.)
# heapq는 기본적으로 min heap이다. 큰 쪽부터 가는 게 낫다..?

# -39 -37 -29 -28 -6 2 11
# 2개씩 간다고 했을 때 (-39) (-37, -29) (-28, -6) (2, 11)
# 39 + 37 * 2 + 28 * 2 + 11 * 2
# (-39, -37) (-29, -28) (-6) (2, 11)
# 39 + 29 * 2 + 6 * 2 + 11 * 2
# 큰것부터 두개씩 묶어서 가는 것이 더 덜 걸린다.
# 최대 힙으로 만들기 위해서 음수로 넣기!

import heapq
n, m = map(int, input().split())
array = list(map(int, input().split()))

theLargest = max(max(array), (-min(array)))

plus = []
minus = []
for number in array:
    if number > 0:
        heapq.heappush(plus, -number) # 양수는 클 수록 절대값이 크다. 따라서 반대로 넣어줘 야한다.
    else:
        heapq.heappush(minus, number)

result = 0
while plus:
    number = heapq.heappop(plus)
    result += number
    for _ in range(m - 1):
        if plus:
            heapq.heappop(plus)


while minus:
    number = heapq.heappop(minus)
    result += number
    for _ in range(m - 1):
        if minus:
            heapq.heappop(minus)

print(2 * -result - theLargest)



