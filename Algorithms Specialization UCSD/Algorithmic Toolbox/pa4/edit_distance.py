# Uses python3
def edit_distance(s, t):
    #write your code here
    s,t = list(s), list(t)
    distance = [[i+j if i==0 or j==0 else 0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    for i in range(1,1+len(t)):
        for j in range(1,1+len(s)):
            insertion = distance[i][j-1] + 1
            deletion = distance[i-1][j] + 1
            match = distance[i-1][j-1]
            mismatch = distance[i-1][j-1] + 1
            if t[i-1] == s[j-1]:
                distance[i][j] = min(insertion, deletion, match)
            else:
                distance[i][j] = min(insertion, deletion, mismatch)
    return distance[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
