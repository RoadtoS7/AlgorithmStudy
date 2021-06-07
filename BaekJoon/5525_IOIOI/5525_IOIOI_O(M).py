N, M = int(input()), int(input())
S = input()

i = 1
count = 0
answer = 0
while i < M:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        count += 1
        if count == N:
            answer += 1
            count -= 1
        i += 1
    else:
        count = 0
    i += 1
print(answer)
