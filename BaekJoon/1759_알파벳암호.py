from itertools import combinations

vowels = ('a', 'i', 'o', 'u', 'e')
l, c = map(int, input().split(' '))

alphabet = input().split()
alphabet.sort()

for password in combinations(alphabet, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if count >= 1 and count <= l - 2:
        print(''.join(password))

