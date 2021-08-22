while True:
    try:
        a = input()
        b = input()
        a, b = set(a), set(b)
        alphabets = a.intersection(b)
        print(''.join(sorted(alphabets)))
    except EOFError:
        break
