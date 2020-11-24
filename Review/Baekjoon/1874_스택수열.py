n = int(input())

stack = []
result = []
current = 1

for i in range(1, n+1):
    num = int(input())
    while current <= num:
        stack.append(current)
        current += 1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result))