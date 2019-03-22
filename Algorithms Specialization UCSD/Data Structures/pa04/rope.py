# python3

import sys

class Vertex:
    """Vertex of a splay tree."""

    def __init__(self, key, value, left, right, parent):
        self.key, self.value, self.left, self.right, self.parent = \
            key, value, left, right, parent


class SplayTree:
    """Splay tree implementation."""

    @staticmethod
    def update(v):
        """Updates sum attribute of the given vertex."""
        if v is None:
            return
        if v.left is not None:
            v.left.parent = v
        if v.right is not None:
            v.right.parent = v

    @classmethod
    def _small_rotation(cls, v):
        parent = v.parent
        if parent is None:
            return
        grandparent = v.parent.parent
        if parent.left == v:
            m = v.right
            v.right = parent
            parent.left = m
        else:
            m = v.left
            v.left = parent
            parent.right = m
        cls.update(parent)
        cls.update(v)
        v.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    @classmethod
    def _big_rotation(cls, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
            # Zig-zig
            cls._small_rotation(v.parent)
            cls._small_rotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            # Zig-zig
            cls._small_rotation(v.parent)
            cls._small_rotation(v)
        else:
            # Zig-zag
            cls._small_rotation(v)
            cls._small_rotation(v)

    @classmethod
    def splay(cls, v):
        """Makes splay of the given vertex and makes it the new root."""
        if v is None:
            return None
        while v.parent is not None:
            if v.parent.parent is None:
                cls._small_rotation(v)
                break
            cls._big_rotation(v)
        return v

    @classmethod
    def find(cls, root, key):
        """Searches for the given key in the tree with the given root
        and calls splay for the deepest visited node after that.
        Returns pair of the result and the new root.
        If found, result is a pointer to the node with the given key.
        Otherwise, result is a pointer to the node with the smallest
        bigger key (next value in the order).
        If the key is bigger than all keys in the tree,
        then result is None.
        """
        v = root
        last = root
        next_ = None
        while v is not None:
            if v.key >= key and (next_ is None or v.key < next_.key):
                next_ = v
            last = v
            if v.key == key:
                break
            if v.key < key:
                v = v.right
            else:
                v = v.left
        root = cls.splay(last)
        return next_, root

    @classmethod
    def split(cls, root, key):
        """Splits the tree into two subtrees by given integer.
        Returns two roots of the left and right subtrees correspondingly.
        """
        result, root = SplayTree.find(root, key)
        if result is None:
            return root, None
        right = cls.splay(result)
        left = right.left
        right.left = None
        if left is not None:
            left.parent = None
        cls.update(left)
        cls.update(right)
        return left, right

    @classmethod
    def merge(cls, left, right):
        """Merges two trees by given vertices.
        Returns new root.
        """
        if left is None:
            return right
        if right is None:
            return left
        while right.left is not None:
            right = right.left
        right = cls.splay(right)
        right.left = left
        cls.update(right)
        return right

    @classmethod
    def inOrder(cls, root):
        cls.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        cls.in_order_traversal(root)
        return cls.result

    @classmethod
    def in_order_traversal(cls, node):
        if node.left != None:
            cls.in_order_traversal(node.left)
        if node.value != None:
            cls.result.append(node.value)
        if node.right != None:
            cls.in_order_traversal(node.right)
        return


class Rope:
    def __init__(self, s):
        self.s = s
    def result(self):
        return self.s
    def process(self, i, j, k):
        # Write your code here

#         substring = self.s[i:j+1]
#         self.s = self.s[:i] + self.s[j+1:]
#         if k == 0:
#             self.s = substring + self.s
#         else:
#             self.s = self.s[:k] + substring + self.s[k:]

    def insert(self, key, value):
        """Inserts integer into the set."""
        left, right = SplayTree.split(self.root, key)
        new_vertex = None
        if right is None or right.key != key:
            new_vertex = Vertex(key, value, None, None, None)
        self.root = SplayTree.merge(SplayTree.merge(left, new_vertex), right)


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
