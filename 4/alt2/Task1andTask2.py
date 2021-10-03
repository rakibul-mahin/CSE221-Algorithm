import heapq

r = open('input1.txt','r')
w = open('output1.txt','w')
w2 = open('output2.txt','w')

def create_graph(graph, node1=None, node2=None, weight=None):
    if node2 == None and weight == None:
        graph[node1] = []
        return graph
    
    if node1 not in graph:
        graph[node1] = []
    
    if node2 not in graph:
        graph[node2] = []
        
    graph[node1].append((node2, weight))
    
    return graph
    
def Dijkstra(graph, source):
    length = len(graph) + 1
    
    dist = [999999] * length
    dist[source] = 0
    
    prev = [0] * length
    prev[source] = 0
    
    visited = [False] * length
    
    Q = []

    for v in graph:
        heapq.heappush(Q,(dist[v], v))

    while len(Q) != 0:
        dist_from_source_for_vertex, the_vertex = heapq.heappop(Q)
        
        if visited[the_vertex] == True:
            continue
        
        visited[the_vertex] = True
        
        for n in graph[the_vertex]:
            alt = dist_from_source_for_vertex + n[1]
            
            if alt < dist[n[0]]:
                dist[n[0]] = alt
                prev[n[0]] = the_vertex
                heapq.heappush(Q, (dist[n[0]], n[0]))
                
    return dist, prev
        
g ={}

data = list()

for i in r:
    data.append(i.replace("\n",""))
    
testCase = int(data[0])
data.pop(0)
    
k = 0
for i in data:
    info = i.split()
    
    if len(info) == 3:
        k += 1
        continue
    
    for j, l in enumerate(info):
        info[j] = int(l)
    
    place = info[0]
    edges = info[1]
    
    if edges == 0:
        g = create_graph(g, place)
        dist, prev = Dijkstra(g,1)
        w.write(str(dist[-1])+"\n")
        w2.write(str(1)+"\n")
        k += 1
    else:
        three_line_data = data[k+1:k+1+edges]
        for i in three_line_data:
            temp = i.split()
            for y, z in enumerate(temp):
                temp[y] = int(z)
                
            p1 = temp[0]
            p2 = temp[1]
            weight = temp[2]
            
            g = create_graph(g, p1, p2, weight)
        
        dist, prev = Dijkstra(g, 1)
        w.write(str(dist[-1])+"\n")
        
        last_index = len(g)
        path = ''
        path_list = []
        
        while last_index != 1:
            path_list.append(str(prev[last_index]))
            last_index = prev[last_index]
            
        path_list = path_list[::-1]
        
        for i in path_list:
            path += i+" "
            
        w2.write(path+str(len(g))+" \n")
        
        k += 1
        
    g = {}

r.close()
w.close()
w2.close()