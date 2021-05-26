word = input()
result = []
for w in word:
    if w.isupper():
        result.append(w.lower())
    else:
        result.append(w.upper())