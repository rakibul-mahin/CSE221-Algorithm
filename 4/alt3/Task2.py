import heapq

def Dijkstra(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(999999)
    dist[source] = 0
    
    Q = []
    
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
        
    prev = []
    for i in range(len(Graph)+1):
        prev.append(0)
    
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))

    while len(Q) != 0:
        u, l = heapq.heappop(Q)
        
        if visited[l]:
            continue
        
        visited[l] = True
        
        for v in Graph[l]:
            alt = u + v[1]
            
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = l
                heapq.heappush(Q, (dist[v[0]], v[0]))
                 
    return prev

g1 = {
    1: []
}

g2 = {
    1: [[2, 10]],
    2: []
}

g3 = {
    3: [[5,1]],
    1: [[2,1], [4,2]],
    2: [[3,4],[5,5]],
    4: [[3,2]],
    5: []
}

w = open('output2.txt','w')

test_case_1 = Dijkstra(g1, 1)
test_case_2 = Dijkstra(g2, 1)
test_case_3 = Dijkstra(g3, 1)

last = len(g1)
w.write("1\n")

last = len(g2)

while last != 1:
    w.write(str(last)+" ")
    last = test_case_2[last]
    
w.write("1\n")

last = len(g3)

while last != 1:
    w.write(str(last)+" ")
    last = test_case_3[last]
    
w.write("1\n")