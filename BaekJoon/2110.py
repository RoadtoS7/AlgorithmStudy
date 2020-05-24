import  sys

N, C = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline) for _  in range(N)]

home.sort()

def routerInstall(distance):
    count = 1
    cur_home = home[0] # 공유기가 설치된 집
    for i in range(1, N):
        if distance <= home[i] - cur_home: # 공유기를 설치하고자 하는 집과의 간격이 더 크기 때문에 공유기 설치 가능
            count += 1
            cur_home = home[i]
    return count

# 공유기 개수를 넘겨줬을 때, 적절한 간격을 찾아주는 함수
def BinarySerach(target):
    start = 1
    end = home[-1] - home[0]

    while start <= end:
        mid = (start+end) // 2
        router_cnt = routerInstall(mid)
        if router_cnt < target: # 공유기 개수가 모자라면, 목표 간격을 좁힌다.
            end = mid - 1
        elif router_cnt >= target: # 공유기를 목표치 이상으로 설치할 수 있다면, 정답이 될 수 있다.
            answer = mid
            start = mid + 1
    return answer

print(BinarySerach(C))