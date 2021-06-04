from collections import deque

N, K = map(int, input().split())
numbers = deque([i for i in range(2, N + 1)])


count = 0
while numbers:
    P = deque.popleft(numbers)

    count += 1
    if count == K:
        print(P)
        exit(0)

    i = 2
    while P * i <= N:
        if P * i in numbers:
            numbers.remove(P * i)
            count += 1

            if count == K:
                print(P * i)
                exit(0)
        i += 1


