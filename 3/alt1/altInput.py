'''
def create_map(nodes, dictionary):
    for n in nodes:
        dictionary[n] = []
        
    return dictionary
        
def create_adj_list(edges, dictionary, count = 0):
    for i in dictionary:
        dictionary[i] = edges[count]
        count += 1
        
    return dictionary
'''

fr = open('altinput.txt','r')

all_lines = fr.read().splitlines()
num_of_nodes = int(all_lines[0])
all_lines = all_lines[1:]

all_nodes = []
all_edges = []
my_dict = {}
count = 0

for i in all_lines:
    data = i.split()
    
    all_nodes.append(int(data[0]))
    data = data[1:]
    for i in range(len(data)):
        data[i] = int(data[i])
    all_edges.append(data)
    
#my_dict = create_map(all_nodes, my_dict)
#my_dict = create_adj_list(all_edges, my_dict)

for n in all_nodes:
        my_dict[n] = []

for i in my_dict:
        my_dict[i] = all_edges[count]
        count += 1

fr.close()