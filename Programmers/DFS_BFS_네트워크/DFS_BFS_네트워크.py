from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)

    for i in range(n):
        answer += bfs(i, graph, visited)

    return answer

def bfs(node, graph, visited):
    count = 0
    if not visited[node]:
        q = deque([node])
        count += 1

        while q:
            new_node = q.pop()
            if not visited[new_node]:
                visited[new_node] = True
                for adj in graph[new_node]:
                    q.append(adj)
    return count
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
