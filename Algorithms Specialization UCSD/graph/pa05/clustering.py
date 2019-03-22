#Uses python3
import sys
import math

def compute_edges(x, y):
    # computes all possible undirected edges between as given set of points
    # takes in lists of x values and y values
    # returns undirected edges and their distances (weights)
    edges, weights = [], []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if [i, j] not in edges:
                edges.append([i,j])
                xdiff, ydiff = x[i]-x[j], y[i]-y[j]
                weights.append(math.sqrt(xdiff**2 + ydiff**2))
    return edges, weights


def find(disjoint_set, u):
    for k in disjoint_set.keys():
        if u in disjoint_set[k]:
            return k

def union(disjoint_set, u, v):
    roots = []
    for k in disjoint_set.keys():
        if u in disjoint_set[k]:
            roots.append(k)
        if v in disjoint_set[k]:
            roots.append(k)
    if roots[0] != roots[1]:
        if roots[0] > roots[1]:
            roots[0], roots[1] = roots[1], roots[0]
        disjoint_set[roots[0]] += disjoint_set[roots[1]]
        del disjoint_set[roots[1]] 


def clustering(x, y, k):
    #write your code here

    # compute all possible segments and their weights 
    segments, weights = compute_edges(x, y)
    # sort according to weights
    id = sorted(range(len(weights)), key=lambda k: weights[k])
    segments = [segments[i] for i in id]
    weights.sort()

    # create MSTs clusters using Kruskal's algo, k disjoint sets
    disjoint_set = {k:[k] for k in [i for i in range(len(x))]}
    min_dist = 0
    while segments:
        if len(disjoint_set.keys()) == k -1:
            # beaking at k -1 means the last edge used connects two clusters
            break		# last edge added is the min d
        s,w = segments.pop(0), weights.pop(0)
        if find(disjoint_set, s[0]) != find(disjoint_set, s[1]):
            union(disjoint_set, s[0], s[1])
            min_dist = w
    return min_dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
#    print(clustering(x,y,k))
    print("{0:.9f}".format(clustering(x, y, k)))
