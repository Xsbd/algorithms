# python3
import sys

def compute_prefix(p):
  s = [0]*len(p)
  border = 0
  for i in range(1,len(p)):
    while border > 0 and p[i] != p[border]:
      border = s[border -1]
    if p[i] == p[border]:
      border = border +1
    else:
      border = 0
    s[i] = border
  return s

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  S = pattern + '$' + text
  s = compute_prefix(S)
  start, stop = len(pattern) +1, len(S)
  for i in range(start, stop):
    if s[i] == len(pattern):
      result.append(i - 2*len(pattern))
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

