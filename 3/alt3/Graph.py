class Graph:

    # This is the constructor that will create a graph with only nodes/vertices
    def __init__(self, Nodes, is_directed=False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        for node in self.nodes:
            self.adj_list[node] = []

    # This is just a tester class of mine to print and check the graph visually
    def print_adj_list(self):
        for node in self.nodes:
            print(node, ":", self.adj_list[node])

    # This is to add path/edge to existing nodes
    def add_edge(self, vertex, edge):
        self.adj_list[vertex].append(edge)
        if not self.is_directed:
            self.adj_list[edge].append(vertex)