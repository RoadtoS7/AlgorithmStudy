from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

def dfs():
    need_visit = deque([n])
    while need_visit:
        now_pos = need_visit.popleft()
        if now_pos == k:
            return array[now_pos]
        else:
            for new_pos in (now_pos + 1, now_pos - 1, now_pos * 2):
                if 0 <= new_pos < MAX and not array[new_pos]:
                    array[new_pos] = array[now_pos] + 1
                    need_visit.append(new_pos)

print(dfs())