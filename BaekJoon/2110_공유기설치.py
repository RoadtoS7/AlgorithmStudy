n, c = list(map(int, input().split(' ')))

array = []
for _ in range(n):
    array.append(int(input()))
array = sorted(array)


start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    value = array[0]

    for i in range(1, len(array)):
        if array[i] >= value + mid:
            count += 1
            value = array[i]

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)