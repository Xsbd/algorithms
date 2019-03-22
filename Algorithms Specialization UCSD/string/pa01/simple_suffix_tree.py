# python3
import sys

class Node:
    def __init__ (self):
        self.out, self.destination = [], []

    def has_out(self, symb):
        #check if a node has an outgoing edge with the given symbol
        if symb in self.out:
                return True
        return False

    def get_dest(self, symb):
        return self.destination[self.out.index(symb)]

    def add_dest(self, node,  symb):
        self.destination.append(node)
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


def compress_branches(node):
    if node.out == ['$']:
        return node.out[0]
    outs = []
    for b in node.out:
        o = compress_branches(node.get_dest(b))
        if len(o) == 1:
            if not isinstance(o[0], list):
                b += o[0]
            else:
                b = [b, o]
        elif len(o) != 0:
            b = [b, o]
        outs.append(b)
    print(outs)
    for o in outs:
        if isinstance(o, list):
            while len(o[1])==1 and isinstance(o[1], list):
                if isinstance(o[1][0], list):
#                    print(type(o[0]),type(o[1][0][0]))
                    o[0] += o[1][0][0]
                    o[1] = o[1][0][1]
                else:
                    break
    print(outs)
    print()
    return outs


def to_string(tree):
    result = []
    while tree:
        if isinstance(tree[0], list):
            result += to_string(tree[0])
        else:
            result.append(tree[0])
        tree = tree[1:]
    return result


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result = []
    # Implement this function yourself
    # build a trie out of text
    patterns = []
    while len(text):
        patterns.append(text)
        text = text[1:]
    tree = build_trie(patterns)
    # compress trie
    tree = compress_branches(tree)
    result = to_string(tree)
    #print(result)
    return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
