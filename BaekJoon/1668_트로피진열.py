n = int(input())

trophy = [int(input()) for _ in range(n)]

left_big = trophy[0]
left_result = 1

for index in range(1, n):
    if trophy[index] > left_big:
        left_result += 1
        left_big = trophy[index]
print(left_result)

right_big = trophy[n-1]
right_result = 1

for index in range(n-1, -1, -1):
    if trophy[index] >right_big:
        right_result += 1
        right_big = trophy[index]

print(right_result)