case = int(input())
for _ in range(case):
    log = input()

    left, right = [], []
    for key in log:
        if key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append(right.pop())
        elif key == '-':
            if left:
                left.pop()
        else:
            left.append(key)

    right.reverse()
    left.extend(right)
    print(''.join(left))
