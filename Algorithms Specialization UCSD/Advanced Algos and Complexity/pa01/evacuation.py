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


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    
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

    # calculate the flow
    for id in graph.get_ids(0) :
        edge = graph.get_edge(id)
        flow += edge.flow

    return flow


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
