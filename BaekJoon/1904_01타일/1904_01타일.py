from sys import stdin

n = int(stdin.readline().rstrip('\n'))

before = 1
value = 2
for i in range(3, n + 1):
    temp = value
    value = value + before
    before = temp

print(value)
