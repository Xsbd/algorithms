#Uses python3
import sys
import math

def minimum_distance(x, y):
    result = 0.
    #write your code here

    # compute all possible segments and their weights
    segments, weights = [], []
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if [i,j] not in segments:
                segments.append([i,j])
                xdiff, ydiff = x[i]-x[j], y[i]-y[j]
                weights.append(math.sqrt(xdiff**2 + ydiff**2))

    # use Kruskal's mst, start with a disjoint set with all vertices as their own set.
    disjoint_set = {k:[k] for k in [i for i in range(len(x))]}    #dict as disjoint_set constructed fron list of vertices

    # sort the edges by weight
    id = sorted(range(len(weights)), key=lambda k: weights[k])
    segments = [segments[i] for i in id]
    weights.sort()

    # Union operations
#    print(disjoint_set)
    for i,s in enumerate(segments):
        if disjoint_set[s[0]] != disjoint_set[s[1]]:
            # equivalent to disjoint set's find (used dict)
            result += weights[i]
            # union operation (change root of one)
            if disjoint_set[s[1]] < disjoint_set[s[0]]:
                old_root,new_root = disjoint_set[s[0]], s[1]
                disjoint_set[s[0]] = disjoint_set[s[1]]
            else:
                old_root,new_root = disjoint_set[s[1]], s[0]
                disjoint_set[s[1]] = disjoint_set[s[0]]
            for k in disjoint_set.keys():
                if disjoint_set[k] == old_root:
                    disjoint_set[k] = disjoint_set[new_root]
           # print('joining', s[0], s[1])
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
