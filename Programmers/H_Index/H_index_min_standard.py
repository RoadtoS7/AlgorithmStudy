def solution(citations):
    citations = sorted(citations)
    n = len(citations)
    for i in range(n):
        # 최대 갯수 = n 값이 h가 되려면, 최소 인용횟수가 n보다 크거나 같아야 한다.
        # n - 1 개가 되려면, 가장 작은 것에서 두번째 꺼(i가 1일 때)가 n - 1보다 크거나 같아야 한다.
        # n - 2개가 되려면, 가장 작은 것에서 세번째 꺼(i가 2일 때)가 n - 2보다 크거나 같아야 한다.
        ## x가 최대 갯수가 되려면 가장 적게 인용된 수가 x보다 크거나 같으면 된다!!!!
        if citations[i] >= n-i:
            return n-i
    return 0