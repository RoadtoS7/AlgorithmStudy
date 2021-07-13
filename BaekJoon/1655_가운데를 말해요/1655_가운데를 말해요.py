import bisect

N = int(input())

number_lst = []
length, mid = 0, 0
for _ in range(N):
    number = int(input())
    bisect.insort_left(number_lst, number)
    length += 1
    if length % 2 == 0:
        mid = length // 2 - 1
    else:
        mid = length // 2

    print(number_lst[mid])