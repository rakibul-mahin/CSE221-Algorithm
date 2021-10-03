from Task1 import create_final_graph
import heapq

#This is similar to Task 1 but only returns the prev array
def Dijkstra(Graph, source, final_dest):
    distances = {vertex: float('infinity') for vertex in Graph}
    distances[source] = 0
    priority_queue = [(0, source)]
    prev = [None for _ in range(final_dest + 1)]
    
    while len(priority_queue) > 0:
        c_dist, c_vert = heapq.heappop(priority_queue)
        
        if c_dist > distances[c_vert]:
            continue
        
        for n, w in Graph[c_vert].items():
            distance = c_dist + w
            
            if distance < distances[n]:
                distances[n] = distance
                prev[n] = c_vert
                heapq.heappush(priority_queue, (distance, n))
           
    for i in range(len(prev)):
            
        if final_dest == 1:
            return "1"
            
        req_str = str(len(prev)-1)
        index = final_dest
            
        while index != 1:
            req_str += str(prev[index])
            index = prev[index]
                
        final = req_str[::-1]
        length = len(final)
        count = 1
            
        req_str = ""
            
        for i in final:
            if count == length:
                req_str += i
            else:
                req_str += i+" "
                    
    return req_str

all_graphs = create_final_graph()

with open("output2.txt","w") as wf:
    for i in all_graphs:
        a = Dijkstra(i, 1, len(i))
        wf.write(a+"\n")