import heapq

r = open('input4.txt','r')
w = open('output4.txt','w')


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

def min_exception(v1, v2):
    if v1 == 0:
        return v2
    if v2 == 0:
        return v1
    
    return min(v1, v2)

def Network(graph, source):
    length = len(graph) + 1
    
    dist = [-999999] * length
    dist[source] = 0
    
    prev = [0] * length
    prev[source] = 0
    
    visited = [False] * length
    
    Q = []

    for v in graph:
        heapq.heappush(Q,(dist[v], v))
        
    heapq._heapify_max(Q)

    while len(Q) != 0:
        dist_from_source_for_vertex, the_vertex = heapq.heappop(Q)
        
        if visited[the_vertex] == True:
            continue
        
        visited[the_vertex] = True
        
        for n in graph[the_vertex]:
            alt = min_exception(dist_from_source_for_vertex, n[1])
            
            if alt > dist[n[0]]:
                dist[n[0]] = alt
                prev[n[0]] = the_vertex
                heapq.heappush(Q, (dist[n[0]], n[0]))
                heapq._heapify_max(Q)
                
    return dist

g = {}

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
    
    if len(info) == 1:
        k += 1
        continue
    
    for j, l in enumerate(info):
        info[j] = int(l)
        
    devices = info[0]
    link = info[1]
    
    if link == 0:
        g = create_graph(g, devices)
        source = int(data[k + link + 1])
        dist = Network(g, source)
        dist.pop(0)
        for i in dist:
            w.write(str(i)+"\n")
        k += 1
    else:
        source = int(data[k + link + 1])
        three_line_data = data[k+1:k+1+link]
        for o in three_line_data:
            temp = o.split()
            for y, z in enumerate(temp):
                temp[y] = int(z)
                
            d1 = temp[0]
            d2 = temp[1]
            rate = temp[2]
            
            g = create_graph(g, d1, d2, rate)
            
        dist = Network(g, source)
        dist.pop(0)
        final_output = ''
        
        for i in dist:
            if i == -999999:
                final_output += str(i+999998)+" "
            else:
                final_output += str(i) + " "
                
        final_output += '\n'
        w.write(final_output)        
        k += 1
        
    g = {}

r.close()
w.close()