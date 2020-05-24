import  sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort()

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start+end) // 2
    wifi_count = 1
    cur_house = house[0]
    for i in range(1, N):
        if mid <= house[i] - cur_house:
            wifi_count += 1
            cur_house = house[i]

    if wifi_count< C:
        end = mid - 1
    elif wifi_count >= C:
        answer = mid
        start = mid + 1
print(answer)

