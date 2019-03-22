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

def varnum(i, k):
    return 3*(i-1) + k

def exactly_one(i, clauses, colors):
    literals = [varnum(i, k) for k in colors]
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def adj(i, j, clauses, colors):
    for k in colors:
        clauses.append([-varnum(i, k), -varnum(j, k)])

def printEquisatisfiableSatFormula():
    clauses = []
    colors = range(1,4)

    for i in range(1,n+1):
        exactly_one(i, clauses, colors)

    for i,j in edges:
        adj(i,j, clauses, colors)

    print(len(clauses), n*3)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

printEquisatisfiableSatFormula()
