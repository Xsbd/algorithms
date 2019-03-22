# python3
import sys

def BWT(text):
    bwt_matrix = []
    for i in range(len(text)):
        prefix, suffix = text[i:], text[:i]
        bwt_matrix.append(prefix + suffix)
    l = [b[-1] for b in sorted(bwt_matrix)]
    result = ''
    for i in l:
        result += i
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
