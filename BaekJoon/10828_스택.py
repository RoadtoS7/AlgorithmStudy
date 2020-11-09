from sys import stdin
times = int(stdin.readline())

stack = []
point = -1

for _ in range(times):
    command = stdin.readline().strip().split(' ')
    if command[0] == "push":
        command[1] = int(command[1])
        stack.append(command[1])
        point += 1
    elif command[0] == "pop":
        if point >= 0:
            print(stack[point])
            del stack[point]
            point -= 1
        else:
            print(-1)

    elif command[0] == "size":
        print(point+1)
    elif command[0] == "empty":
        if point == -1:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if point >= 0:
            print(stack[point])
        else:
            print(point)

