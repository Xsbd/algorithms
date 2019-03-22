#Uses python3

import sys

def largest_number(a):
    #write your code here
    ans = []
    a = [int(i) for i in a]
    while a:
        maxN = 0 
        for n in a:
            if is_greater_or_equal(n, maxN):
                maxN = n
        ans.append(maxN)
        a.remove(maxN)
    res = ""
    for x in ans:
        res += str(x)
    return res

def is_greater_or_equal(n, maxN):
    a = n*10**(len(str(maxN))) + maxN
    b = maxN*10**(len(str(n))) + n
    return a>=b

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

