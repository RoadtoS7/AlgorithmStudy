n = input()

flag = True
count = 0

for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        if flag:
            count += 1
        flag = not flag


print(count)