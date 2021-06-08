from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
not_hear = set()
not_see = set()
for _ in range(N):
    not_hear.add(input().rstrip('\n'))
for _ in range(M):
    not_see.add(input().rstrip('\n'))

result = not_hear.intersection(not_see)
print(len(result))

for name in list(sorted(result)):
    print(name)
