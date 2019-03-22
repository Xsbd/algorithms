# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum = sum + current

        current, next = next, current + next

    return sum % 10

def fibonacci_sum_seq(n):
    if n <= 1:
        return n

    curr = 0
    next = 1 

    mod_seq = [0]
    seq_validator = []
    tmp = mod_seq
    for _ in range(n):
        if(tmp == mod_seq and tmp == seq_validator):
            break
        tmp.append(next%10)
        curr, next = next, curr+next
        if(next%10 == 0 and (curr+next)%10 == 1):
            mod_seq, tmp = tmp, seq_validator

    return mod_seq

def fibonacci_partial_sum_fast(from_, to):
    seq = fibonacci_sum_seq(to)
    f, t = (from_ - (from_//len(seq))*len(seq)), (to - (to//len(seq))*len(seq))
    return sum(seq[f:t+1])%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum_fast(from_, to))

