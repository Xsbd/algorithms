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


def PreprocessBWT(bwt):
  """
  Preprocess the Burrows-Wheeler Transform bwt of some text
  and compute as a result:
    * starts - for each character C in bwt, starts[C] is the first position 
        of this character in the sorted array of 
        all characters of the text.
    * occ_count_before - for each character C in bwt and each position P in bwt,
        occ_count_before[C][P] is the number of occurrences of character C in bwt
        from position 0 to position P inclusive.
  """
  # Implement this function yourself
  
  idx = [i for i in range(len(bwt))]
  starts = {}
  occ_counts_before = {}
  for i,l in enumerate(sorted(bwt)):
    if l not in starts.keys():
      starts[l] = i

  for i,l in enumerate(bwt):
    for key in occ_counts_before.keys():
      occ_counts_before[key] += [occ_counts_before[key][-1]]
    if l not in occ_counts_before.keys():
      occ_counts_before[l] = [0] * (i+1) + [1]
    else:
      occ_counts_before[l][-1] += 1

  #print(starts, occ_counts_before)
  return starts, occ_counts_before


def FindOccurrences(pattern, bwt, starts, occ_counts_before, suffix_array):
  """
  Find the occurrences of string pattern in the text
  given only suffix_array, Burrows-Wheeler Transform bwt of the text and additional
  information we get from the preprocessing stage - starts and occ_counts_before.
  """
  # Implement this function yourself
  top = 0
  bottom = len(bwt) -1
  while top <= bottom:
    if pattern:
      symbol = pattern[-1]
      pattern = pattern[:-1]
      if symbol in bwt[top:bottom+1]:
         top = starts[symbol] + occ_counts_before[symbol][top]
         bottom = starts[symbol] + occ_counts_before[symbol][bottom+1] -1
      else:
         return ''
    else:
      result = []
      for i in range(top, bottom +1):
        result.append(suffix_array[i])
      return result


def pattern_matching_with_suffix_array(text, pattern, suffix_array):
    min_idx = 0
    max_idx = len(text)
    p_len, t_len = len(pattern), len(text)
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx)//2
        s = suffix_array[mid_idx]
        e = (s +p_len if (s +p_len) < t_len else t_len)
        #print(s,e, pattern, text[s:e], pattern > text[s:e])
        if pattern > text[s:e]:
            min_idx = mid_idx +1
        else:
            max_idx = mid_idx
    start = min_idx
    #print(start)
    max_idx = len(text)
    while min_idx < max_idx:
        mid_idx = (min_idx + max_idx)//2
        s = suffix_array[mid_idx]
        e = (s +p_len if (s +p_len) < t_len else t_len)
        #print(s, e, pattern, text[s:e], pattern < text[s:e])
        if pattern < text[s:e]:
            max_idx = mid_idx
        else:
            min_idx = mid_idx +1
    end = max_idx
    #print(end)
    if start > end:
        return ''
    else:
        result = []
        for i in range(start, end):
            result.append(suffix_array[i])
        return result


def find_occurrences(text, patterns):
    occs = set()
    text += '$'
    suffix_array = build_suffix_array(text)
    '''
    bwt = [0]*len(suffix_array)
    for i,s in enumerate(suffix_array):
        c = s - 1
        if c < 0:
            c = len(suffix_array)-1
        bwt[i] = text[c]
    starts, occ_counts_before = PreprocessBWT(bwt)
    '''
    for pattern in patterns:
       #occs.update(FindOccurrences(pattern, bwt, starts, occ_counts_before, suffix_array))
       occs.update(pattern_matching_with_suffix_array(text, pattern, suffix_array))
    return occs


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))
