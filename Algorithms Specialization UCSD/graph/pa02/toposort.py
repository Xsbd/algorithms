#Uses python3

import sys

clock = 0

def previsit(pre, v):
    global clock
    pre[v] = clock
    clock += 1

def postvisit(post, v):
    global clock
    post[v] = clock
    clock += 1

def explore(adj, visited, pre, post, v):
    visited[v] = 1
    previsit(pre, v)
    for w in adj[v]:
        if not visited[w]:
            explore(adj, visited, pre, post, w)
    postvisit(post, v)

def dfs(adj, used, order):
    #write your code here
    visited, pre, post = used, used, used
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, visited, pre, post, v)
    order = {p:v for v,p in enumerate(post)}
    order = [order[k] for k in sorted(order.keys())]
    order.reverse() 
    return order

def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    return dfs(adj, used, order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

