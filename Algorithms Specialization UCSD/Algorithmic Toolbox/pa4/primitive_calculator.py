# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_optimal_sequence(n):
    all_prev = [None]*(n+1)
    all_min_op = [0]+[None]*n

    for i in range(1,n+1):
        curr = i -1
        min_op = all_min_op[curr] + 1

        if i%3 == 0:
            num_op = all_min_op[i//3] +1
            if num_op < min_op:
                curr, min_op = i//3, num_op

        if i%2 == 0:
            num_op = all_min_op[i//2] +1
            if num_op < min_op:
                curr, min_op = i//2, num_op

        all_prev[i], all_min_op[i] = curr, min_op

    sequence = []
    i = n
    while i > 0:
        sequence.append(i)
        i = all_prev[i]
    sequence.reverse()

    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(dp_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
