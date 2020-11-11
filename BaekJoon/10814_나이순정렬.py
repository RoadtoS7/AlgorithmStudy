n = int(input())

members = list()
for i in range(n):
    info = input().split(' ')
    members.append([int(info[0]), info[1], i])

members.sort(key= lambda x: (x[0], x[2]))

for member in members:
    print(member[0], member[1])