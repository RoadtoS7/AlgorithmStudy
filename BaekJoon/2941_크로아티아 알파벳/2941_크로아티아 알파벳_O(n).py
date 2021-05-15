first = {'c', 'd', 'n', 'l', 's', 'z'}
cro = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
word = input()

i = 0
result = 0
while i < len(word):
    result += 1
    if word[i] in first:
        if word[i:i + 2] in cro:
            i += 2
            continue

        if word[i:i + 3] in cro:
            i += 3
            continue
    i += 1

print(result)