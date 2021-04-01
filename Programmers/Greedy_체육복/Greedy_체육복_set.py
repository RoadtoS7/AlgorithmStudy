## 이렇게 바꾼 이유:
# list 에서 in 연산은 O(n)의 시간이 소모된다고 한다.
# 또한 list의 remove() 연산은 O(n)의 소모된다고 한다.
# 반연에 set에서 in 연산은 O(1)의 시간이 소모되며,
# remove() 연산은 O(1)의 시간이 소모된다.
def solution(n, lost, reserve):
    # isHave = [1] * (n + 1)
    real_lost = set(lost) - set(reserve)
    # for item in real_lost:
    #     isHave[item] = 0

    real_reserve = set(reserve) - set(lost)
    # real_reserve.sort()

    # for item in real_reserve:
    #     if item - 1 >= 1 and not isHave[item - 1]:
    #         isHave[item - 1] = True
    #         continue
    #
    #     if item + 1 <= n and not isHave[item + 1]:
    #         isHave[item + 1] = True
    # return sum(isHave) - 1

    for item in real_reserve:
        if item - 1 in real_lost:
            real_lost.remove(item -1)
            continue
        if item + 1 in real_lost:
            real_lost.remove(item + 1)

    return n - len(real_lost)

print(solution(5, [2, 4], [1, 3, 5]))