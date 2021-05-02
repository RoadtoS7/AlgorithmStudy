from sys import stdin
input = stdin.readline

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    before, after = 1, 2
    for i in range(3, N + 1):
        temp = before + after
        before = after % 15746
        after = temp % 15746
    print(after)


