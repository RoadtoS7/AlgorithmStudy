T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = [s*R for s in S]
    print(''.join(result))


