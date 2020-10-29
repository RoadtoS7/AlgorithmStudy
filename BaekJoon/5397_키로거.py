from sys import stdin
case = int(stdin.readline())

for _ in range(case):
    leftstack = list()
    rightstack = list()
    log = input()

    for data in log:
        if data == '<':
            if leftstack:
                data = leftstack.pop()
                rightstack.append(data)
        elif data == '>':
            if rightstack:
                data = rightstack.pop()
                leftstack.append(data)
        elif data == '-':
            if leftstack:
                leftstack.pop()
        else:
            leftstack.append(data)

    leftstack.extend(reversed(rightstack))
    print("".join(leftstack))



