# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    k, l = n, 1 
    while(k>2*l):
        summands.append(l)
        k, l = k-l, l+1
    if k!=0:
        summands.append(k)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
