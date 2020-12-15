bird = int(input())
result = 0
sing = 1

while bird > 0:
    if bird - sing < 0:
        sing = 1
    bird = bird - sing
    result += 1
    sing += 1

print(result)