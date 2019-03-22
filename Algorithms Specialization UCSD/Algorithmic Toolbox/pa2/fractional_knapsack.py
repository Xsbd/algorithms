# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    values = [values[i]/weights[i] for i in range(len(values))]
    ind = sorted(range(len(values)), key=lambda k: values[k], reverse=1)
    values = sorted(values, reverse=1)
    weights = [weights[v] for _,v in enumerate(ind)]
    for i,v in enumerate(values):
        if weights[i] > capacity:
            value += v*capacity
            break
        value += v*weights[i]
        capacity -= weights[i]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
