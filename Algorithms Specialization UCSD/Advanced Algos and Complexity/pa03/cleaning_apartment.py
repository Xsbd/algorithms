# python3
import itertools

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

'''
# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula():
    print("3 2")
    print("1 2 0")
    print("-1 -2 0")
    print("1 -2 0")

printEquisatisfiableSatFormula()
'''


def varnum(i, j):
    return n*i + j

def exactly_one(literals, clauses):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def printEquisatisfiableSatFormula():
    clauses = []
    positions = range(1,n+1)
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i-1].append(j-1)
        adj[j-1].append(i-1)

    for i in range(n):
        exactly_one([varnum(i, j) for j in positions], clauses)

    for j in positions:
        exactly_one([varnum(i, j) for i in range(n)], clauses)

    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            clauses.append([-varnum(i, j)] + [varnum(n, j+1) for n in nodes])

    print(len(clauses), n*n)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

printEquisatisfiableSatFormula()
