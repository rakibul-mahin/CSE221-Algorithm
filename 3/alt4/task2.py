def BFS(v, g, n, e):
    
    wf = open('output2.txt','w')
    wf.write("Places:")
    
    q = []
    v[int(n)-1] = 1
    q.append(n)
    
    length = len(q)
    
    while length != 0:
        m = q.pop(0)
        wf.write(" "+str(m)+" ")
        
        if int(m) == int(e):
            break
        
        for n in g[int(m)]:
            if not v[int(n)-1]:
                v[int(n)-1] = 1
                q.append(n)
        
    


file = open('input1.txt','r')
data = file.read()
li = data.split()
total_place = int(li[0])
total_con = int(li[1])
li = li[2:]

graph = [[]for i in range(total_place + 1)]

for i in range(0, len(li)-1, 2):
    node = int(li[i])
    v = int(li[i+1])
    graph[node].append(v)

finalGraph = {}
graph = graph[1:]
for i, j in enumerate(graph):
    finalGraph[i+1] = j

visited = [0] * total_place
BFS(visited, finalGraph, '1', '12')
file.close()