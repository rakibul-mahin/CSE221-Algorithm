# Importing some required variables from Task1
from Task1 import graph, total_vertices

# This is the implementation of the pseudocode given in the question
def DFS_VISIT(graph, node):
    visited[int(node) - 1] = 1
    printed.append(node)

    for each_node in graph.adj_list[node]:
        if each_node not in visited:
            DFS_VISIT(graph, each_node)

# This is the implementation of the pseudocode given in the question
def DFS(graph, endPoint):

    with open('output3.txt', 'w') as write_file:

        write_file.write("Places: ")

        for each_node in graph.adj_list:
            if each_node not in visited:
                DFS_VISIT(graph, each_node)

        # This will write the output file till we reach the End point for the first time
        for i in printed:
            if i != int(endPoint):
                write_file.write(str(i)+" ")
            else:
                write_file.write(str(i))
                break


# Driver Code
visited = [0] * total_vertices
printed = []
DFS(graph, '12')