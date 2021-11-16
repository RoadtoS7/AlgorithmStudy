N, C = map(int, input().split())

house = [int(input()) for _ in range(N)]
house.sort()
end, start = house[-1] - house[0], 1
result = 0

while end >= start:
    mid = (end + start) // 2
    count, last_ap_location = 1, house[0]

    for location in house[1:]:
        if last_ap_location + mid <= location:
            count += 1
            last_ap_location = location

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)