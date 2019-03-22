#Uses python3

import sys

sys.setrecursionlimit(200000)

clock = 0
pre = []
post = []

def previsit(v):
    global clock, pre
    pre[v] = clock
    clock += 1

def postvisit(v):
    global clock, post
    post[v] = clock
    clock += 1

def explore(adj, visited, v):
    visited[v] = True
    previsit(v)
    for w in adj[v]:
        if not visited[w]:
            explore(adj, visited, w)
    postvisit(v)

def dfs(adj):
    global pre, post
    visited = [0 for _ in range(len(adj))]
    pre, post = visited, visited
    for v in range(len(adj)):
        if not visited[v]:
            explore(adj, visited, v)

def number_of_strongly_connected_components(adj):
    global post
    result = 0 
    #write your code here

    # compute the reverse graph i.e. the reverse adj matrix
    reverse_adj = [[] for _ in range(len(adj))]
    for n,vl in enumerate(adj):
        for v in vl:
            reverse_adj[v].append(n)

    # dfs on reverse graph
    dfs(reverse_adj)

    visited = [0 for _ in range(len(adj))]
    post_order = {p:v for v,p in enumerate(post)}
    post_order = [post_order[k] for k in sorted(post_order.keys())]
    reverse_post_order = post_order[::-1]
    # post_order.reverse() reverses post_order and returns none
    for v in reverse_post_order:
        if not visited[v]:
            explore(adj, visited, v)
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
    print(number_of_strongly_connected_components(adj))
