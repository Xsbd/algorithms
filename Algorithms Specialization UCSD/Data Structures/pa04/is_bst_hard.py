#python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if not tree:
    return True
  return isBST(tree, 0, -(2**31), (2**31))

def isBST(tree, n, min, max):
  if n < 0:
    return True
  if tree[n][0] < min or tree[n][0] > max:
    return False
  return (isBST(tree, tree[n][1], min, tree[n][0]-1) 
and isBST(tree, tree[n][2], tree[n][0], max))

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
