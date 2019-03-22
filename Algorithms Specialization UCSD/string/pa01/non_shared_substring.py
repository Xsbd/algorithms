# python3
import sys
sys.setrecursionlimit(4000)

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

    def all_non_common_stree_dfs(self, node):
        if not node.out:
            if '#' not in node.label:
                return '$'
            if node.label[0] != '#':
                return node.label[0] + '#'
            return '#'
        leaves = []
        for key in node.out.keys():
            leaves.append(self.all_non_common_stree_dfs(node.out[key]))
        if '$' not in leaves:	# all leaves contain part of text1
            type_i_node = [l for l in leaves if '##' in l]
            if not type_i_node:		# node contains only leaves
                return node.label + '#'
        else:			# some leaves with only text2 present
            while '$' in leaves:
                leaves.remove('$')
            while '#' in leaves:
                leaves.remove('#') # can't use just the path to this node due to '$' only branch
        if leaves:
            leaves = [l.split('#')[0] for l in leaves]
            leaves = [l for l in leaves if l != '']
            if leaves:
                ret = min((l for l in leaves), key=len)
            else:
                ret = ''
            if node.label:
                return node.label + ret + '##'
            return min((l for l in leaves), key=len)
        return '$'

    def get_shortest_non_common(self):
        l = self.all_non_common_stree_dfs(self.root)
        return l


def solve (p, q):
    tree = SuffixTree(p+'#'+q+'$')
    result = tree.get_shortest_non_common()
    return result
    

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
