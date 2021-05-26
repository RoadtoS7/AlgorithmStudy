name = input()
names = name.split('-')
result = []
for name in names:
    result.append(name[0])
print(''.join(result))