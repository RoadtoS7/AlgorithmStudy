from collections import deque


def bfs(start, ticket_count, graph):
    q = deque([(start, [start], set())])
    result_path = []

    while q:
        node, path, used_tickets = q.pop()
        if ticket_count == len(used_tickets):
            result_path.append(path)
            continue

        if node not in graph:
            continue

        for adj, ticket_id in graph[node]:
            if ticket_id not in used_tickets:
                new_path = path[:]
                new_path.append(adj)

                new_used_tickets = used_tickets.copy()
                new_used_tickets.add(ticket_id)
                q.append((adj, new_path, new_used_tickets))

    return result_path


def solution(tickets):
    answer = []
    graph = dict()

    for index, ticket in enumerate(tickets):
        source, destination = ticket
        if source not in graph:
            graph[source] = [(destination, index)]
        else:
            graph[source].append((destination, index))

    answer = bfs("ICN", len(tickets), graph)

    answer.sort()
    return answer[0]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
