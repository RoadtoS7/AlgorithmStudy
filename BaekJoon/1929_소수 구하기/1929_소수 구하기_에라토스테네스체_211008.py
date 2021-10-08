import math
from collections import defaultdict

M, N = map(int, input().split())

def get_all_prime(start, end):
    is_prime = [True] * (end + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(math.sqrt(end)) + 1):
        if is_prime[i]:
            j = 2
            while i * j <= end:
                is_prime[i * j] = False
                j += 1

    for i in range(start, end + 1):
        if is_prime[i]:
            print(i)

get_all_prime(
M, N
)