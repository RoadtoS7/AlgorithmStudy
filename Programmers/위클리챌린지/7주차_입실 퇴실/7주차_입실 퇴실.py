def solution(enter, leave):
    N = len(enter)

    answer = [0] * N
    enter_index = 0
    room = set()


    for l in leave:
        ## 나간 사람이 room에 존재하는지 검사
        while l not in room:
            ## 존재하지 않는다면, enter 배열에서 나간 사람까지를 전부 room에 넣어준다.
            room.add(enter[enter_index])
            enter_index += 1
        ## 나간 사람을 room에서 없앤다.
        room.remove(l)

        ## 현재 room에 있는 사람은 현재 나간 사람과 반드시 만난 것이기 때문에, 나간 사람의 개수인 1만큼을 answer에서 증가시킨다.
        for person in room:
            answer[person - 1] += 1

        ## 현재 나간 사람은 현재 room에 남아있는 사람과는 반드시 만난 것이기 때문에, 현재 room에 남아있는 사람의 개수를 더해준다.
        answer[l - 1] += len(room)

    return answer

print(solution([1,3,2], [1, 2, 3]))
