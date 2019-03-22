#Uses python3

import sys

def explore(visited, adj, v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(visited, adj, w)
    return

def number_of_components(n, adj):
    result = 0 
    #write your code here
    visited = [0 for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            explore(visited, adj, v)
            result += 1
    return result

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
    print(number_of_components(n, adj))
