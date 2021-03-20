def solution(name):
    change = [min(ord(letter) - ord('A'), ord('Z') - ord(letter) + 1) for letter in name]
    i, answer = 0, 0

    while True:
        answer += change[i]
        change[i] = 0

        if sum(change) == 0:
            return answer

        left, right = 1, 1
        while change[i - left] == 0:
            left += 1

        while change[i + right] == 0:
            right += 1

        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right

print(solution(input()))
