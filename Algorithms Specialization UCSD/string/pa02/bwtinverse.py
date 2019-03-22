# python3
import sys

def InverseBWT(bwt):
    # write your code here
    idx = [i for i in range(len(bwt))]
    sorted_id = sorted(range(len(bwt)), key=lambda x: bwt[x])

    # map which letters corresponds to which between sorted_bwt and bwt
    fl_map = {f: l for f,l in zip(idx, sorted_id)}
    
    # build the word
    word = ''
    next = fl_map[0]
    for _ in range(len(bwt)):
        # letter prefix to the word is added 
        word += bwt[next]
        # find the exact occurance of l in sorted_bwt
        next = fl_map[next]
    return word[1:] + '$'


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
