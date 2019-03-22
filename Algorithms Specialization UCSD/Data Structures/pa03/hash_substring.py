# python3

from random import randint

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return rabin_karp(pattern,text)

def rabin_karp(pattern, text):
    big_prime = 500003
    x = randint(1,big_prime-1)
    result = []
    pHash = poly_hash(pattern, big_prime, x)
    H = precompute_hashes(text, len(pattern), big_prime, x)
#    print(pHash)
#    print(H)
    for i in range(0,len(text) -len(pattern) +1):
        if pHash != H[i]:
            continue
        if are_equal(text[i:i+len(pattern)], pattern):
            result.append(i)
    return result

def poly_hash(string, p, x):
    hash = 0
    for i in range(len(string)-1,-1,-1):
        hash = (hash * x + ord(string[i])) % p
    return hash

def precompute_hashes(text, p_size, big_prime, x):
    H = [None] * (len(text) - p_size +1)
    S = text[(len(text) - p_size):]				# last substring
    H[len(text) - p_size] = poly_hash(S, big_prime, x)		# hash of last substring
    y = 1
    for i in range(1, p_size +1):
        y = (y * x) % big_prime					# hash for first substring
    for i in range(len(text) -p_size -1, -1, -1):
        H[i] = (x * H[i+1] + ord(text[i]) - y * ord(text[i+p_size])) % big_prime
    return H

def are_equal(s1,s2):
    return (s1 == s2)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

