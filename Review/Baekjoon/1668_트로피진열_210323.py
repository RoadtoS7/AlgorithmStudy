N = int(input())
trophies = []
for _ in range(N):
  trophies.append(int(input()))

can_see, left_count = trophies[0], 1
for trophy in trophies[1:]:
    if can_see < trophy:
        left_count += 1
        can_see = trophy

can_see, right_count = trophies[-1], 1
for index in range(len(trophies) - 1, -1, -1):
    if can_see < trophies[index]:
        right_count += 1
        can_see = trophies[index]

print(left_count, right_count, end='\n')
