# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.in_order_traversal(0)
    return self.result

  def in_order_traversal(self, n):
    if self.left[n] != -1:
      self.in_order_traversal(self.left[n])
    self.result.append(self.key[n])
    if self.right[n] != -1:
      self.in_order_traversal(self.right[n])
    return

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.pre_order_traversal(0)
    return self.result

  def pre_order_traversal(self, n):
    self.result.append(self.key[n])
    if self.left[n] != -1:
      self.pre_order_traversal(self.left[n])
    if self.right[n] != -1:
      self.pre_order_traversal(self.right[n])
    return

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.post_order_traversal(0)
    return self.result

  def post_order_traversal(self, n):
    if self.left[n] != -1:
      self.post_order_traversal(self.left[n])
    if self.right[n] != -1:
      self.post_order_traversal(self.right[n])
    self.result.append(self.key[n])
    return

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
