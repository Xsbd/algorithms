#Uses python3

import sys
import queue

def bfs(adj, s, t):
    dist = [1000000 for _ in range(len(adj))]
    dist[s] = 0
    queue = [s]
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == 1000000:
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[t] < 1000000:
        return dist[t]
    return -1

def distance(adj, s, t):
    #write your code here
    return bfs(adj, s, t)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
