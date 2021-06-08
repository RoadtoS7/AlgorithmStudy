N, M = map(int, input().split())
people = {}
for _ in range(N + M):
    person = input()
    if person in people:
        people[person] += 1
    else:
        people[person] = 1

result = []

for person, count in people.items():
    if count == 2:
        result.append(person)
print(len(result))
result.sort()
for name in result:
    print(name)
