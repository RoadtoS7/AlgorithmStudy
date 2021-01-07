import sys

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

if max(crane) < max(box):
    print(-1)
    sys.exit()

crane.sort(reverse=True)
box.sort(reverse=True)
crane_to_box = [0] * n
moved_box = [False] * m

result = 0
count = 0
while True:
    if count == len(box):
        break
    for i in range(n):
        while crane_to_box[i] < len(box):
            if not moved_box[crane_to_box[i]] and crane[i] >= box[crane_to_box[i]]:
                moved_box[crane_to_box[i]] = True
                crane_to_box[i] += 1
                count += 1
                break

            crane_to_box[i] += 1
    result += 1

print(result)