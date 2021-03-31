
def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if (yellow // i + i) * 2 == brown - 4:
                return [yellow // i + 2, i + 2]