count = int(input())

result = 0
lang = list()

for i in range(count):
    newLang = list(input())
    lang.append(newLang)

    newone = lang[len(lang) - 1]

    now = ''
    before = list()
    isAll = True

    for j in newone:
        if isAll:
            if j != now:
                if j in before:
                    isAll = False
                    break
                else:
                    before.append(now)
                    now = j

        else:
            break

    if isAll:
        result += 1

print(result)






