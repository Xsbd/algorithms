#Uses python3

import sys

def explore(visited, adj, v):
    visited[v] = True
    for w in adj[v]:
        explore(visited, adj, w)

def dfs(adj, n):
    visited = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            explore(visited, adj, v)

def acyclic(adj, n):
    try:
        dfs(adj, n)
        return 0
    except:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
