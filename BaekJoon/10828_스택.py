n = int(input())

stack = [0] * n
top_index = -1

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        top_index += 1
        stack[top_index] = command[1]

    elif command[0] == 'top':
        print(stack[top_index])
    elif command[0] == 'size':
        print(top_index + 1)
    elif command[0] == 'empty':
        if top_index != -1:
            print(0)
        else:
            print(1)
    else:
        if top_index != -1:
            print(stack[top_index])
            stack[top_index] = 0
            top_index -= 1
        else:
            print(top_index)
