# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    x = get_majority_element(a, left, (left+right)//2)
    y = get_majority_element(a, (left+right)//2, right)
    if x==y:
        return x
    else:
        xcount, ycount = 0,0
        for i in range(left, right):
            if a[i] == x:
                xcount += 1
            if a[i] == y:
                ycount += 1
        if xcount > (right-left)//2:
            return x
        if ycount > (right-left)//2:
            return y
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
