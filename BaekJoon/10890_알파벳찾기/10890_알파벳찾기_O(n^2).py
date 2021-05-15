from string import ascii_lowercase

word = input()
alphabet = {a:-1 for a in ascii_lowercase}
for w in word:
    i = word.find(w)
    if alphabet[w] == -1:
        alphabet[w] = i





