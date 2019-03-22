# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions = merge(a,left,ave,right)
    return number_of_inversions

def merge(a, l, m, r):
    n1 = m - l
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = a[l + i]
 
    for j in range(0 , n2):
        R[j] = a[m + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    pairs = i
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
        pairs -= 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

    return pairs


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
