def count_gap(start, end):
    count = 0
    
    for A in range(start + 1, end - 1):
        for B in range(A + 1, end):
            if A <= n <= B:
                count += 1

    return count


L = int(input())
S = list(map(int, input().split()))
n = int(input())
count = 0

if n in S:
    print(0)
    exit(0)

S.sort()
if n < S[0]:
    print(count_gap(0, S[0]))
    exit(0)


i, start, end = 0, -1, -1
while i < L - 1:
    if S[i] < n < S[i + 1]:
        start = S[i]
        end = S[i + 1]
        break
    else:
        i += 1

print(count_gap(start, end))
