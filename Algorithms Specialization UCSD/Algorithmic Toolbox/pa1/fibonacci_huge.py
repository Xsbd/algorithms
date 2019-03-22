# Uses python3
import sys

def get_fibonacci_huge_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

def pisano(m):
    prev = 0
    curr = 1
    length = 2
    for _ in range(m*m):
        prev, curr = curr % m, (curr+prev) % m
        if(curr%m == 0 and (curr+prev)%m == 1):
            break
        length += 1

    return length

def get_fibonacci_huge_fast(n,m):
    r = n % pisano(m)
    return get_fibonacci_huge_naive(r) % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    #print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge_fast(n, m))
#    for n in range(1000000000000000000):
#        for m in range(2,100000):
#            if get_fibonacci_huge_naive(n,m) != get_fibonacci_huge_fast(n, m):
#                print('wrong!')
#                break

