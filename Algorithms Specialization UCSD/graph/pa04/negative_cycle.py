#Uses python3

import sys

def relax(adj, cost, dist, prev, u, v):
    v_id = adj[u].index(v)
    if dist[v] > dist[u] + cost[u][v_id]:
        dist[v] = dist[u] + cost[u][v_id]
        prev[v] = u


def negative_cycle(adj, cost):
    # using bellman-ford algorithm

    # fill in distance and predecessor array
    dist = [float('inf')]*len(adj)
    prev = [None]*len(adj)
    dist[0] = 0

    # relax edges |V| -1 times
    for _ in range(len(adj) -1):	# repeat |V|-1 times
        for u in range(len(adj)):	# all edges 
            for v in adj[u]:		# all edges
                relax(adj, cost, dist, prev, u, v)
        if float('inf') in dist:
            dist[dist.index(float('inf'))] = 0

    # detect negative cycle
    for u in range(len(adj)):
        for v in adj[u]:
            if dist[u] != float('inf') and dist[v] > dist[u]+ cost[u][adj[u].index(v)]:
                return 1
    return 0 


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
    print(negative_cycle(adj, cost))
