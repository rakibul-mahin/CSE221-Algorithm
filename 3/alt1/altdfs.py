import altInput

def DFS_VISIT(g, n):
    visited[int(n)-1] = 1
    printed.append(n)
    
    for nodes in g[n]:
        if nodes not in visited:
            DFS_VISIT(g, nodes)
            
def DFS(g, e):
    wf = open('altdfs.txt','w')
    wf.write("Places: ")
    
    for n in g:
        if n not in visited:
            DFS_VISIT(g, n)
            
    for i in range(0, len(printed)):
        if str(printed[i]) == e:
            wf.write(str(printed[i])+" ")
            break
        else:
            wf.write(" "+str(printed[i])+" ")
            
    wf.close()
            

total = altInput.num_of_nodes
graph = altInput.my_dict
visited = [0] * total
printed = []
DFS(graph, "12")