from Graph import Graph
import heapq

#This is the Dijkstra Algorithm
def Dijkstra(Graph, source, final_dest):
    #Distances will contain all the shortest distances from 1/source
    distances = {vertex: float('infinity') for vertex in Graph}
    #Making the distances[source] = 0, because the distance from source to source is 0
    distances[source] = 0
    #This is to create a priotity queue
    priority_queue = [(0, source)]
    
    while len(priority_queue) > 0:
        #Popping elements from priority queue
        #Returning a Tuple, first = distance and second = the source
        #For example c_dist is the distance of source to c_vert 
        c_dist, c_vert = heapq.heappop(priority_queue)
        
        #Comparing the current c_dist with any existing distances for that c_vert
        #If existing distance is less than the c_dist we will continue
        if c_dist > distances[c_vert]:
            continue
        
        #Calculating the distacne with the weight + c_dist
        for n, w in Graph[c_vert].items():
            distance = c_dist + w
            
            #Comparing the new distance and updating the distances
            if distance < distances[n]:
                distances[n] = distance
                heapq.heappush(priority_queue, (distance, n))
                 
    for i in distances:
        if i == final_dest:
            return str(distances[i])
    
#Taking Inputs
#It will create a graph like
# g = {
#    1: {{2: 3},{3: 2}}
#}   
def create_final_graph():
    
    with open('input1.txt', 'r') as r:
        with open('output1.txt', 'w') as w:
            
            g = Graph()
            
            all_graphs = []
            
            all_lines = r.read().splitlines()
            total_test_cases = int(all_lines[0])
            all_lines = all_lines[1:]
            
            count = 1
            
            for i in range(len(all_lines)):
                
                temp = all_lines[i].split()
                length = len(temp)
                
                if length == 2:
                    total_nodes, total_edges = int(temp[0]), int(temp[1])
                
                if length == 3:
                    i += 1
                elif total_nodes == 1:
                    g.map[total_nodes] = {}
                    a = Dijkstra(g.map, 1, total_edges)
                    if count == total_test_cases:
                        w.write(str(0))
                    else:
                        w.write(str(0)+"\n")
                        
                    all_graphs.append(g.map)
                    
                    g = Graph()
                    i += 1
                    count += 1
                elif total_nodes > 1:
                    next_index = i+1
                    
                    for _ in range(total_edges):
                        n1, n2, weight, next_index = g.get_info(next_index, all_lines)
                        
                        g.map = g.add_info(total_edges, n1, n2, weight)
                
                    a = Dijkstra(g.map, 1, total_nodes)

                    if count != total_test_cases:
                        w.write(a+"\n")
                        count += 1
                    else:
                        w.write(a)

                    i += 1
                    all_graphs.append(g.map)
                    g = Graph()
                    
    return all_graphs
                    
create_final_graph()