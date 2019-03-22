# Uses python3
import sys

def get_change(m):
    #write your code here
    tens = m // 10
    fives = (m - tens*10) // 5
    ones = (m - tens*10 - 5*fives)
    m = tens + fives + ones
    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
