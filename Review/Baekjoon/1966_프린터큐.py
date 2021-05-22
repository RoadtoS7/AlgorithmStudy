case = int(input())

for _ in range(case):
    documents, priorities = [], []
    N, M = map(int, input().split())
    for i, priority in enumerate(map(int, input().split())):
        priorities.append(priority)
        documents.append((i, priority))
    priorities.sort(reverse=True)

    count = 0
    for max_priority in priorities:
        while True:
            order, priority = documents.pop(0)
            if priority == max_priority:
                count += 1
                break
            else:
                documents.append((order, priority))
        if order == M:
            break

    print(count)