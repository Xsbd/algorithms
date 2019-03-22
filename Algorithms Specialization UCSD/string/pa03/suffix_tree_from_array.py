# python3
import sys

self_idx = 0

class SuffixTreeNode:
    def __init__(self, idx, parent_id, children, depth, start, end):
        self.idx, self.parent_id = idx, parent_id
        self.children = children
        self.depth, self.start, self.end = depth, start, end

def create_new_leaf(node, S, suffix):
    global self_idx
    self_idx += 1
    leaf = SuffixTreeNode(self_idx, node.idx, {}, len(S) -suffix, suffix +node.depth, len(S) -1)
    node.children[S[leaf.start]] = leaf.idx
    return leaf

def break_edge(tree, node, S, start, offset):
    global self_idx
    self_idx += 1

    start_char = S[start]
    mid_char = S[start + offset]

    # create a new node to insert
    mid_node = SuffixTreeNode(self_idx, node.idx, {}, node.depth +offset, start, start +offset-1)
    mid_node.children[mid_char] = node.children[start_char]

    idx = node.children[start_char]
    # make child of previous node the child of new node
    tree[idx].parent_id = mid_node.idx
    tree[idx].start += offset

    # make the new node the child of previous node
    node.children[start_char] = mid_node.idx
    tree.append(mid_node)

    return mid_node


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    tree = []
    # Implement this function yourself
    root = SuffixTreeNode(0, -1, {}, 0, -1, -1)
    lcp_prev = 0
    cur_node, tree = root, [root]
    for i in range(len(text)):
        suffix = sa[i]
        while cur_node.depth > lcp_prev:
            cur_node = tree[cur_node.parent_id]
        if cur_node.depth == lcp_prev:
            cur_node = create_new_leaf(cur_node, text, suffix)
            tree.append(cur_node)
        else:
            start = sa[i-1] + cur_node.depth
            offset = lcp_prev - cur_node.depth
            mid_node = break_edge(tree, cur_node, text, start, offset)
            cur_node = create_new_leaf(mid_node, text, suffix)
            tree.append(cur_node)
        if i < len(text) -1:
            lcp_prev = lcp[i]
    edges = {}
    for node in tree:
        if node.children:
            neighbors = []
            for c in node.children.keys():
                child = tree[node.children[c]]
                neighbors.append([child.idx, child.start, child.end+1])
                neighbors = sorted(neighbors)
            edges.update({node.idx:neighbors})
    return edges


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(0, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if not node in tree:
        continue
      edges = tree[node]
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (edges[edge_index][1], edges[edge_index][2]))
      stack.append((edges[edge_index][0], 0))
