N = int(input())
M = int(input())
S = input()
P = "I"
P += ("OI" * N)
count = 0
for i in range(0, M - (2 *N + 1)):
    if S [ i : i + (2* N + 1)] == P:
        count += 1

print(count)
