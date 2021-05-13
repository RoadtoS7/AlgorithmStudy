L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()
S = [0] + S

if n in S:
    print(0)
    exit(0)

start, end = -1, -1
for s in S:
    if s < n:
        start = s + 1
    else:
        end = s - 1
        break

s_in_end_count = end - start
s_in_gap = (end - n) * (n - start)
print(s_in_end_count + s_in_gap)

