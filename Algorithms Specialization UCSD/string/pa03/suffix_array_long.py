# python3
import sys


def sort_characters(s):
  order = [0]*len(s)
  alpha_map = {'$':0, 'A':1, 'C':2, 'G':3, 'T':4}	# alphabet
  count = [0]*5  	# alphabet contains only 5 chars A, C, G, T, $
  for i in range(len(s)):
    c = alpha_map[s[i]]
    count[c] += 1
  for j in range(1,5):
    count[j] = count[j] + count[j-1]
  for i in range(len(s)-1,-1,-1):	#count down to zero
    c = alpha_map[s[i]]
    count[c] = count[c] -1
    order[count[c]] = i
  return order


def compute_char_classes(s, order):
  cl = [0]*len(s)
  for i in range(1, len(s)):
    if s[order[i]] != s[order[i-1]]:
      cl[order[i]] = cl[order[i-1]] +1
    else:
      cl[order[i]] = cl[order[i-1]]
  return cl


def sort_doubled(S, L, order, cl):
  count = [0]*len(S)
  new_order = [0]*len(S)
  for i in range(len(S)):
    count[cl[i]] += 1
  for j in range(1, len(S)):
    count[j] = count[j] + count[j-1]
  for i in range(len(S)-1, -1, -1):
    start = (order[i] - L + len(S)) % len(S)
    c = cl[start]
    count[c] = count[c] -1
    new_order[count[c]] = start
  return new_order


def update_classes(new_order, cl, L):
  n = len(new_order)
  new_class = [0]*n
  for i in range(1,n):
    cur, prev = new_order[i], new_order[i-1]
    mid, mid_prev = (cur + L) % n, (prev + L) % n
    if cl[cur] != cl[prev] or cl[mid] != cl[mid_prev]:
      new_class[cur] = new_class[prev] +1
    else:
      new_class[cur] = new_class[prev]
  return new_class


def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """

  # Implement this function yourself
  order = sort_characters(text)
  cl = compute_char_classes(text, order)
  L = 1
  while L < len(text):
    order = sort_doubled(text, L, order, cl)
    cl = update_classes(order, cl, L)
    L = 2*L
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
