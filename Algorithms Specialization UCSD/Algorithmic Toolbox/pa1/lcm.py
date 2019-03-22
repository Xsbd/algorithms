# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    return gcd(a, b) * int((a / gcd(a, b))) * int((b / gcd(a, b)))

def gcd(a, b):
    if b > a:
        a, b = b, a
    while(b!=0):
        a, b = b, a%b
    return int(a) 

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a,b))

