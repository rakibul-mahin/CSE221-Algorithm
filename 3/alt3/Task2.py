# Importing some required variables from Task1
from Task1 import graph, total_vertices

# This is the implementation of the pseudocode given in the question for BFS
def BFS(visited, graph, node, endPoint):
    queue = []
    visited[int(node) - 1] = 1
    queue.append(node)
    with open('output2.txt','w') as write_file:
        write_file.write("Places:"+" ")

        # This will run till the queue is empty
        while len(queue) != 0:
            m = queue.pop(0)
            write_file.write(str(m)+" ")

            # This is to check whether I have reached the endpoint
            if int(m) == int(endPoint):
                break
            
            # Here we will explore the nodes connected with
            for neighbor in graph.adj_list[int(m)]:
                if not visited[int(neighbor) - 1]:
                    visited[int(neighbor) - 1] = 1
                    queue.append(neighbor)

# Driver Code
visited = [0] * total_vertices
BFS(visited, graph, '1', '12')