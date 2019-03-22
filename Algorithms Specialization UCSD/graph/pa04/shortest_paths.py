#Uses python3

import sys
import queue


def relax(adj, cost, distance, reachable, u, v):
    v_id = adj[u].index(v)
    if distance[v] > distance[u] + cost[u][v_id]:
        distance[v] = distance[u] + cost[u][v_id]
        reachable[v] = 1


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    queue = []
    visited = [False]*len(adj)

    # |V| -1 iterations
    for _ in range(len(adj) -1):
        for u in range(len(adj)):
            for v in adj[u]:
                relax(adj, cost, distance, reachable, u, v)

    # |V| th iteraton
    for u in range(len(adj)):
        for v in adj[u]:
            v_id = adj[u].index(v)
            if distance[v] > distance[u] + cost[u][v_id]:
                queue.append(v)

    # process all rechable nodes from nodes in -ve loop
    while queue:
        u = queue.pop(0)
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v] and v not in queue:
                queue.append(v)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

