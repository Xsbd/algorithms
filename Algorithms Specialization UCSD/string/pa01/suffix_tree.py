# python3
import sys

class SuffixTree:
    class Node:
        def __init__ (self, label):
            self.label = label	# label on path leading to this node
            self.out = {}	# outgoing edges

    def __init__(self, s):
        """ Make suffix tree """
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)	# trie for longest suffix
        # add the rest of suffixes, from longest to shortest
        for i in range(1,len(s)):
            # start at root; we'll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    label = child.label
                    # Walk along edge until we exhaust edge label or until we missmatch
                    k = j+1
                    while k-j < len(label) and s[k] == label[k-j]:
                        k += 1
                    if k-j == len(label):
                        cur = child 	# we exhaust the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = label[k-j], s[k]
                        # create "mid" : new node bisecting edge
                        mid = self.Node(label[:k-j])
                        mid.out[cNew] = self.Node(s[k:])
                        # original child becomes mid's child
                        mid.out[cExist] = child
                        # original child's label is curtailed
                        child.label = label[k-j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell of tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def serialize_stree_dfs(self, node):
        if isinstance(node, str):
            return node
        stree = [node.label if node.label is not None else '']
        for key in node.out.keys():
            stree += self.serialize_stree(node.out[key])
        return stree

    def serialize_stree_bfs(self, node):
        que = [val for val in node.out.values()]
        edges = []
        while que:
            node = que.pop(0)
            if node.out:
                que += [val for val in node.out.values()]
            edges.append(node.label)
        return edges

    def get_stree(self):
        #return self.serialize_stree_dfs(self.root)[1:]
        return self.serialize_stree_bfs(self.root)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    tree = SuffixTree(text)
    result = tree.get_stree()
    #print(result)
    return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
