from itertools import permutations
from math import sqrt
from math import ceil


def solution(numbers):
    candidates = set()
    for i in range(1, len(numbers) + 1):
        for number_tuple in list(permutations(numbers, i)):
            candidates.add(int(''.join(number_tuple)))

    answer = 0
    for number in candidates:
        if number == 0 or number == 1:
            continue
        is_prime = True
        for i in range(2, ceil(sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            answer += 1

    return answer

print(solution('17'))