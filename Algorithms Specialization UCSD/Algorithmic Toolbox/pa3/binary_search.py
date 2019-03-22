# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    return b_search(a, x, left, right-1)

def b_search(a, x, low, high):
    if high < low:
        return -1
    mid = low + int((high - low)//2)
    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return b_search(a, x, low, mid-1) 
    elif a[mid] < x:
        return b_search(a, x, mid+1, high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
