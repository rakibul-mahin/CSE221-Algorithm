# Importing some required variables from Task1
from Graph import Graph

# This is a function that helps me to read data
# This will return 3 variables of
    # 1. List of all the vertexes/nodes/places
    # 2. List of all edges/path/connections
    # 3. Total number of vertexes/nodes/places
def open_file(name, mode):
    with open(name, mode) as read_file:
        all_lines = read_file.read().splitlines()
        total_lines = int(all_lines[0])
        all_lines = all_lines[1:]

        vertex = []
        edges = []

        for i in all_lines:
            temp = i.split()
            node = int(temp[0])
            vertex.append(node)
            temp = temp[1:]

            for j in temp:
                temp_list = []
                temp_list.append(node)
                temp_list.append(int(j))

                edges.append(temp_list)

    return vertex, edges, total_lines


# Driver Code
v, e, total_vertices = open_file('input1.txt', 'r')
graph = Graph(v, is_directed = True)

#Here n stands for nodes/vertices and p stands for path/edges
for n, p in e:
    graph.add_edge(n, p)

#This is just to show the created graph
graph.print_adj_list()