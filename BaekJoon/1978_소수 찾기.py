# O(n제곱)
# def is_prime(number):
#     if  number == 1:
#         return False
#
#     m = number ** 0.5
#     for i in range(2, m + 1):
#         if number % i == 0:
#             return False
#     return True

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))

count = 0
for number in numbers:
    if is_prime(number):
        count += 1

print(count)
