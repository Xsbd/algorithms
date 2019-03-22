# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                # maxHeight = 0
                # for vertex in range(self.n):
                #        height = 0
                #        i = vertex
                #        while i != -1:
                #                height += 1
                #                i = self.parent[i]
                #        maxHeight = max(maxHeight, height);
                # return maxHeight;

                if not self.parent:
                        return 0
                root = self.parent.index(-1)
                self.children = {k:[] for k in range(self.n)}
                for k,v in enumerate(self.parent):
                        if v in self.children:
                                self.children[v].append(k)
                nodes = [root]
                height, next_inc = 0, 1
                while nodes:
                        node = nodes.pop(0)
                        next_inc -= 1
                        children = self.children[node]
                        nodes += children
                        if next_inc == 0:
                                next_inc = len(nodes)
                                height += 1
                return height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
