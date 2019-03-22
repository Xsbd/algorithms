#Uses python3

import sys
import queue

def bipartite(adj):
    dist = [1000000 for _ in range(len(adj))]
    dist[0] = 0
    que = [0] 		# start at source node as 1
    while que:
       u = que.pop(0)
       for v in adj[u]:
           if dist[v] == 1000000:
               que.append(v)
               dist[v] = dist[u] + 1
               for w in adj[v]:
                   if dist[w] == dist[v]:
                       return 0
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
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
