# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum = sum + current

    return sum%10

def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1

    mod_seq = [0]
    seq_validator = []
    tmp = mod_seq
    for _ in range(n):
        if(tmp == mod_seq and tmp == seq_validator):
            break
        tmp.append(curr%10)
        prev, curr = curr, prev+curr
        if(curr%10 == 0 and (curr+prev)%10 == 1):
            mod_seq, tmp = tmp, seq_validator

    return sum(mod_seq[ : (n - (n//len(mod_seq))*len(mod_seq) +1) ]) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_fast(n))
