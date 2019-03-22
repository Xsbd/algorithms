# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    while table != parent[table]:
        table = parent[table]
    return parent[table]

def merge(destination, source, lines):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size

    if rank[realSource] >= rank[realDestination]:
        parent[realSource] = realDestination
    else:
        parent[realDestination] = realSource
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1

    lines[realSource], lines[realDestination] = 1, lines[realDestination] + lines[realSource]
    return True    

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1, lines)
    ans = max(lines)
    print(ans)
