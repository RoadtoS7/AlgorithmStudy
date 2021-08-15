case = int(input())
inputs = [int(input()) for _ in range(case)]
cache = [0] * 11
cache[0], cache[1], cache[2], cache[3] = 0, 1, 2, 4

top = 3
for input in inputs:
    if input <= top:
        print(cache[input])
    else:
        for i in range(top + 1, input + 1):
            cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
        top = input
        print(cache[input])


