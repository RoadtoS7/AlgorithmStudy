document, term = input(), input()

term_length, i, count = len(term), 0, 0
while i < len(document):
    if document[i] == term[0] and document[i:i + term_length] == term:
        count += 1
        i += term_length
    else:
        i += 1

print(count)
