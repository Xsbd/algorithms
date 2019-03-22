# python3
n, m = list(map(int, input().split()))
A = []
for i in range(n):
  A += [list(map(int, input().split()))]
b = list(map(int, input().split()))

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n,m,A,b):
    '''
    print("3 2")
    print("1 2 0")
    print("-1 -2 0")
    print("1 -2 0")
    '''
    clauses = []

    for i, coeffs in enumerate(A):
        nz_cf = [(j, coeffs[j]) for j in range(m) if 0 != coeffs[j]]
        l = len(nz_cf)
        for x in range(2**l):
            currSet = [nz_cf[j] for j in range(l) if 1 == ((x/2**j)%2)//1]
            currSum = 0
            for coeff in currSet:
                currSum += coeff[1]
            if currSum > b[i]:
                clauses.append([-(cf[0]+1) for cf in currSet] + [cf[0]+1 for cf in nz_cf if not cf in currSet])

    if 0 == len(clauses):
        clauses.append([1, -1])
        m = 1

    print(len(clauses), m)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

printEquisatisfiableSatFormula(n,m,A,b)
