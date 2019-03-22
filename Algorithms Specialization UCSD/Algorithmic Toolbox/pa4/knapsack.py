# Uses python3
import sys

def optimal_weight(W, w, n):
    # write your code here
    value = [[0 for i in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            value[i][j] = value[i-1][j]
            if w[i-1] <= j:
                value[i][j] = max(w[i-1] + value[i-1][j-w[i-1]], value[i-1][j])
    return value[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
