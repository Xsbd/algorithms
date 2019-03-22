# python3
import sys


class Node:
        def __init__ (self):
                self.out, self.children = [], []

        def has_out(self, symb):
                #check if a node has an outgoing edge with the given symbol
                if symb in self.out:
                        return True
                return False

        def get_dest(self, symb):
                return self.children[self.out.index(symb)]

        def add_dest(self, node,  symb):
                self.children.append(node)
                self.out.append(symb)


def build_trie(patterns):
        root = Node()

        for p in patterns:
                current_node = root
                for i in range(len(p)):
                        current_symbol = p[i]
                        if current_node.has_out(current_symbol): 	#check outgoing edges
                                current_node = current_node.get_dest(current_symbol)
                        else:
                                new_node = Node()
                                current_node.add_dest(new_node, current_symbol)
                                current_node = new_node
        return root


def prefix_trie_matching(text, trie):
        i = 0
        symbol = text[i]
        v = trie
        while 1:
                i += 1
                if not v.out: 		#v is a leaf if v has no outgoing edges
                        return True	# pattern match
                elif symbol in v.out:
                        v = v.get_dest(symbol)
                        if i >= len(text):
                                symbol = '$'
                        else:
                                symbol = text[i]
                else:
                        return False	# no possible pattern match


def solve (text, n, patterns):
        result = []

        # write your code here
        trie = build_trie(patterns)
        i = 0
        while text:
                if prefix_trie_matching(text, trie):
                    result.append(i)
                text = text[1:]
                i += 1

        return result


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
