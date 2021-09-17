def solution(enter, leave):
    N = len(enter)
    leave_idx, enter_idx = 0, 0
    answer = [0] * N
    room = set()

    for leave_one in leave:
        while leave_one not in room:
            room.add(enter[enter_idx])
            enter_idx += 1

        room.remove(leave_one)
        for person in room:
            answer[person - 1] += 1
        answer[leave_one - 1] += len(room)

    return answer

print(solution([1,3,2], [1, 2, 3]))
print(solution([1,4,2,3], [2, 1, 3, 4]))
print(solution([3, 2, 1], [2, 1, 3]))
print(solution([3, 2, 1], [1, 3, 2]))
print(solution([1,4,2,3], [2,1,4,3]))


