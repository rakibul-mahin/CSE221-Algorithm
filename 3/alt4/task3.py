def DFS_VISIT(g, n):
    visited[int(n)-1] = 1
    printed.append(n)
    
    for nodes in g[n]:
        if nodes not in visited:
            DFS_VISIT(g, nodes)
            
def DFS(g, e):
    wf = open('output3.txt','w')
    wf.write("Places:")
    
    for n in g:
        if n not in visited:
            DFS_VISIT(g, n)
            
    for i in range(0, len(printed)):
        if str(printed[i]) == e:
            wf.write(" "+str(printed[i])+" ")
            break
        else:
            wf.write(" "+str(printed[i])+" ")

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
printed = []
DFS(finalGraph, '12')

file.close()