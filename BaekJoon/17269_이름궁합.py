N, M = map(int, input().split())
A, B = input().split()


alpha = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

AB = ""
small_length = min(N, M)
for i in range(small_length):
    AB += A[i] + B[i]

AB += A[small_length:] + B[small_length:] # 슬라이싱으로 남은 문자열을 붙일 수 있다.
# small_length 길이의 문자열은 위 슬라이싱에서 빈 문자열을 반환할것 이기 때문이다.

scores = [alpha[ord(i) - ord('A')] for i in AB]
## AB를 이루는 문자마다 아스키 코드 값을 구해서 A를 빼주면 A를 0번째 인덱스로 했을 때 각 문자의 인덱스를 구할 수 있다.


for i in range(N + M - 2):
    for j in range(N + M -1 - i):
        scores[j] += scores[j + 1]

print('{}%'.format(scores[0] % 10 * 10 + scores[1] % 10))