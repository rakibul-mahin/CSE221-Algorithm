file = open('input1.txt','r')
data = file.read()
li = data.split()
total_place = int(li[0])
total_con = int(li[1])
li = li[2:]

graph = [[] for i in range(total_place + 1)]

for i in range(0, len(li), 2):
    node = int(li[i])
    v = int(li[i+1])
    graph[node].append(v)
    
finalGraph = {}
graph = graph[1:]
print(graph)

for i, j in enumerate(graph):
    finalGraph[i+1] = j

print(finalGraph)
file.close()