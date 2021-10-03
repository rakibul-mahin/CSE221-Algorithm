import altInput

def BFS(v, g, n, e):
    
    wf = open('altbfs.txt','w')
    wf.write("Places: ")
    
    q = []
    v[int(n)-1] = 1
    q.append(n)
    
    length = len(q)
    
    while length != 0:
        m = q.pop(0)
        wf.write(str(m)+" ")
        
        if int(m) == int(e):
            break
        
        for k in g[int(m)]:
            if not v[int(k)-1]:
                v[int(k)-1] = 1
                q.append(k)
    wf.close()

total = altInput.num_of_nodes
graph = altInput.my_dict
visited = [0] * total
BFS(visited, graph, "1", "12")