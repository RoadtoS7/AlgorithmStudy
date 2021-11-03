from sys import stdin
from collections import Counter
input = stdin.readline
N, x = map(int, input().rstrip().split())

numbers = Counter(map(int, input().split()))
if x in numbers:
    print(numbers[x])
else:
    print(-1)
