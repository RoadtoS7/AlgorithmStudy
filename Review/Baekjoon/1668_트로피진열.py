def appending(data):
    result = 1
    top = data[0]
    for i in range(1, len(data)):
        if top < data[i]:
            result += 1
            top = data[i]
    return result

n = int(input())

trophy = []
for _ in range(n):
    trophy.append(int(input()))

print(appending(trophy))
trophy.reverse()
print(appending(trophy))