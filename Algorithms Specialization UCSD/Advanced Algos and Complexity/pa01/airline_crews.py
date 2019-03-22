# python3

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_graph(bipartite_graph):
    n = len(bipartite_graph)
    m = len(bipartite_graph[0])
    vertex_count = n + m + 2
    graph = FlowGraph(vertex_count)
    for i in range(n):
        graph.add_edge(0, i+1, 1)
    for i in range(m):
        graph.add_edge(n+1+i, n+m+1, 1)
    for i in range(n):
        for j in range(m):
            if(not bipartite_graph[i][j]):
                continue
            graph.add_edge(i+1, n+1+j, 1)
    return graph


def max_flow(graph):

    while(True):
        found_path = False
        queue = []
        parentIDs = [-1] * graph.size()
        queue.append(0)

        # BFS
        while (queue and not found_path):
            node = queue.pop(0)
            ids = graph.get_ids(node)
            for id in ids:
                edge = graph.get_edge(id)
                if edge.flow < edge.capacity and parentIDs[edge.v] == -1 :
                    if edge.v == edge.u :
                        continue
                    parentIDs[edge.v] = id
                    if edge.v == (graph.size() -1) :
                        found_path = True
                        break
                    queue.append(edge.v)

        if not found_path :
            break

        to = graph.size() -1
        min_cap = -1
        while to !=0 :
            id = parentIDs[to]
            edge = graph.get_edge(id)
            if (min_cap == -1) or ((edge.capacity - edge.flow) < min_cap) :
                min_cap = edge.capacity - edge.flow
            to = edge.u
        to = graph.size() -1
        while to !=0 :
            id = parentIDs[to]
            edge = graph.get_edge(id)
            graph.add_flow(id, min_cap)
            to = edge.u


class MaxMatching:

    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        '''
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True
        return matching
        '''
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1]*n
        graph = read_graph(adj_matrix)
        max_flow(graph)
        for i in range(n):
            for id in graph.get_ids(i+1):
                edge = graph.get_edge(id)
                if edge.flow == 1 :
                    matching[i] = edge.v - (n + 1)
                    break
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
