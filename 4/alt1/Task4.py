from Graph import Graph
import heapq

#This returns the minimum val between two values
def find_min(val1, val2):
    
    if val1 == 0 and val2 != 0:
        return val2
    
    if val2 == 0 and val1 != 0:
        return val1
    
    if val1 < val2:
        return val1
    else:
        return val2 

#This is the modified code of task1 and task2
def Network(Graph, source):
    distances = {vertex: float('-infinity') for vertex in Graph}
    distances[source] = 0
    priority_queue = [(0, source)]
    heapq._heapify_max(priority_queue)
    
    while len(priority_queue) > 0:
        c_dist, c_vert = heapq.heappop(priority_queue)
        
        if c_dist > distances[c_vert]:
            continue
        
        for n, w in Graph[c_vert].items():
            distance = find_min(c_dist, w)
            
            if distance > distances[n]:
                distances[n] = distance
                heapq.heappush(priority_queue, (distance, n))
                heapq._heapify_max(priority_queue)
                
    return distances

def create_final_network():
    with open('input4.txt','r') as r:
        with open('output4.txt', 'w') as w:
            
            g = Graph()
            all_graphs = []
            
            all_lines = r.read().splitlines()
            total_test_cases = int(all_lines[0])
            all_lines = all_lines[1:]
            
            count = 1
            
            for i in range(len(all_lines)):
                temp = all_lines[i].split()
                print(temp)
                length = len(temp)
                
                if length == 2:
                    total_devices, total_links = int(temp[0]), int(temp[1])
                if length == 3:
                    i += 1
                elif length == 1:
                    i += 1
                elif total_devices == 1:
                    g.map[total_devices] = {}
                    source = int(all_lines[i+1])
                    dist = Network(g.map, source)
                    
                    w.write("0\n")

                    all_graphs.append(g.map)
                    
                    g = Graph()
                    i += 1
                    count += 1
                elif total_devices > 1:
                    next_index = i + 1
                    link_count = 1
                    source = 0
                    for _ in range(total_links):
                        if link_count == total_links:
                            n1, n2, weight, next_index = g.get_info(next_index, all_lines)
                            g.map = g.add_info(total_links, n1, n2, weight)
                            source = int(all_lines[i + total_links + 1])
                        else: 
                            n1, n2, weight, next_index = g.get_info(next_index, all_lines)
                            g.map = g.add_info(total_links, n1, n2, weight)
                            link_count += 1
                        
                    dist = Network(g.map, source)
                    
                    for i in range(1, len(dist)):
                        if dist[i] == float('-infinity'):
                            w.write(str(-1)+" ")
                        else:
                            w.write(str(dist[i])+" ")
                            
                    w.write(str(dist[len(dist)])+"\n")
                            
                    i += 1
                    all_graphs.append(g.map)
                    g = Graph()
                    count += 1
                         
create_final_network()