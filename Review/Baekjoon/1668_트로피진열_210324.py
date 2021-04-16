def count_visible(trophies):
    visible_trophy, result = trophies[0], 1
    for trophy in trophies[1:]:
        if trophy > visible_trophy:
            result += 1
            visible_trophy = trophy
    return result

N = int(input())
trophies = [int(input()) for _ in range(N)]
left_count = count_visible(trophies)
trophies.reverse()
right_count = count_visible(trophies)

print(left_count, right_count, sep='\n')
