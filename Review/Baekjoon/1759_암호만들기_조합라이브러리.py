from itertools import combinations

L, C = map(int, input().split())
vowels = {'a', 'e', 'i', 'o', 'u'}
candidates = input().split()

candidates.sort()
result = []
for cipher in combinations(candidates, L):
    vowels_count = 0
    for cipher_char in cipher:
        if cipher_char in vowels:
            vowels_count += 1

    if vowels_count >= 1 and vowels_count <= L - 2:
        result.append(''.join(cipher))


print('\n'.join(result))
