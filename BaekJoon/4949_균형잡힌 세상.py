

while True:
    words = input()
    stack = []
    if words == ".":
        break
    stable_flag = True
    for word in words:
        if word == "(" or word == "[":
            stack.append(word)
            continue

        elif word == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stable_flag = False
                break

        elif word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stable_flag = False
                break

    if not stable_flag:
        print('no')
    else:
        if stack:
            print('no')
        else:
            print('yes')

