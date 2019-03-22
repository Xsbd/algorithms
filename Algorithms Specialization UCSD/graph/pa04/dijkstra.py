#Uses python3

import sys
import queue

def extract_min(H):
    min_key = sorted(H.keys())[0]
    rval = H[min_key].pop(0)
    if H[min_key] == []:
        del H[min_key]
    return rval

def change_priority(H, v, d):
    if d not in H.keys():
        H[d] = [v]
    else:
        H[d].append(v)

def distance(adj, cost, s, t):
    # dijkstra's algorithm
    dist = [10**9 for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    dist[s] = 0

    # make priority queue to select next node to process
    hash_queue = {} 
    for v,d in enumerate(dist):
        if d in hash_queue.keys():
            hash_queue[d].append(v)
        else:
            hash_queue[d] = [v]

    # process nodes from the priority queue
    while hash_queue:
        u = extract_min(hash_queue)
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
                dist[v] = dist[u] + cost[u][adj[u].index(v)]
                prev[v] = u
                change_priority(hash_queue, v, dist[v])

    # dist list contains distance from s to all connected nodes
    if dist[t] != 10**9:
        return dist[t] 
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
