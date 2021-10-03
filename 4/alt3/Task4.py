import heapq

def Network(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(-999999)
    dist[source] = 0
    
    Q = []
    
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
        
    prev = []
    for i in range(len(Graph)+1):
        prev.append(0)
    prev[source] = 1
    
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))
        
    heapq._heapify_max(Q)
        
    while len(Q) != 0:
        u, l = heapq._heappop_max(Q)
        
        if visited[l] == 1:
            continue
        
        visited[l] = 1
        
        for v in Graph[l]:
            alt = 0
            
            if u == 0:
                alt = v[1]
            elif v[1] == 0:
                alt = u
            elif u < v[1]:
                alt = u
            else:
                alt = v[1]
                
            if alt > dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = l
                
                heapq.heappush(Q, (dist[v[0]], v[0]))
                heapq._heapify_max(Q)
                
    return dist

s1 = 1
g1 = {
    1: []
}

s2 = 1
g2 = {
    1: [[2,1]],
    2: []
}

s3 = 2
g3 = {
    1: [[2,1]],
    2: []
}

s4 = 1
g4 = {
    3: [[2,6], [4,2]],
    1: [[2,3], [3,8]],
    2: [[4,7]],
    4: []
}

w = open("output4.txt", "w")

test_case_1 = Network(g1, s1)
test_case_2 = Network(g2, s2)
test_case_3 = Network(g3, s3)
test_case_4 = Network(g4, s4)

w.write(str(test_case_1[-1])+"\n")

test_case_2 = test_case_2[1:]
for i in test_case_2:
    w.write(str(i)+" ")
w.write("\n")

test_case_3 = test_case_3[2:]
w.write(str("-1")+" ")
for i in test_case_3:
    w.write(str(i)+"\n")
    
test_case_4 = test_case_4[1:]
for i in test_case_4:
    w.write(str(i)+" ") 
w.write("\n")   