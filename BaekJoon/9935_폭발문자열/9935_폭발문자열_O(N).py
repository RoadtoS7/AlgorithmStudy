words, bomb = input(), input()
stack = []
bomb_len, top = len(bomb), 0

for w in words:
    stack.append(w)
    top += 1

    if w == bomb[-1]:
        in_flag = True
        for i in range(bomb_len):
            index = top - bomb_len + i
            if index < 0 or stack[index] != bomb[i]:
                in_flag = False
                break
        if in_flag:
            for i in range(bomb_len):
                stack.pop()
                top -= 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')




