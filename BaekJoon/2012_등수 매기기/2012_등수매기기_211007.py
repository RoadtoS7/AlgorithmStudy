from collections import  deque
N = int(input())

plst = [int(input()) for _ in range(N)]
plst.sort()

rank = 1
q = deque([])
answer = 0

for p in plst:
    if rank == p:
        rank += 1
        continue
    elif rank > p:
        q.append(p)
    else:
        while rank < p and q:
            _q = q.popleft()
            answer += abs(rank - _q)
            rank += 1

        answer += abs(rank - p)
        rank += 1

while q:
    _q = q.popleft()
    answer += abs(_q  - rank)
    rank += 1

print(answer)





