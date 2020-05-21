def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])

                    strElement = ''.join(element)
                    ret.append(strElement)

                else:
                    stack.append(temp)
    ret = list(set(ret))
    return ret


result =dfs_perm("VVHH", 4)
print(result)