def solution(n, lost, reserve):
    isHave = [1] * (n + 1)
    for lost_id in lost:
        if lost_id in reserve:
            reserve.remove(lost_id)
        else:
            isHave[lost_id] = 0

    for reserve_id in reserve:
        before = reserve_id - 1
        if before >= 1 and before <= n:
            if not isHave[before]:
                isHave[before] = 1
                continue

        after = reserve_id + 1
        if after >= 1 and after <= n:
            if not isHave[after]:
                isHave[after] = 1
                continue


    answer = sum(isHave) -1
    return answer