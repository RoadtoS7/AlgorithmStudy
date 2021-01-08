n, S = int(input()), input()

score, bonus = 0, 0
for index, OX in enumerate(S): ## 인덱스와 함게 값을 꺼낼 수 있다.
    if OX == 'O':
        score, bonus = score + (index + 1) + bonus, bonus + 1
    else:
        bonus = 0

print(score)