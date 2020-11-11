n = int(input())

members = list()
for _ in range(n):
    member = input().split(' ')
    members.append(int(member[0], member[1]))

members = sorted(members, key=lambda x: x[0])

for member in members:
    print(member[0], member[1])


