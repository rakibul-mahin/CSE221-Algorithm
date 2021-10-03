r = open('input1.txt', 'r')
w = open('output1.txt', 'w')

data = []

for i in r:
    data.append(i.replace('\n',''))

data.pop(0)
twoD = []

for i in data:
    temp = i.split()
    twoD.append(temp)
    
for i in twoD:
    i[0], i[1] = i[1], i[0]
    
for i, j in enumerate(twoD):
    twoD[i][0] = int(j[0])
    twoD[i][1] = int(j[1])
    
twoD.sort()

for i in twoD:
    i[0], i[1] = i[1], i[0]

final = []
assignment_done = 0

final.append(twoD[0])
assignment_done += 1
become_free = final[0][1]

twoD.pop(0)

for i in twoD:
    if i[0] >= become_free:
        final.append(i)
        assignment_done += 1
        become_free = i[1]
        
w.write(str(assignment_done))
w.write('\n')
for i in final:
    w.write(str(i[0])+" "+str(i[1])+"\n")

r.close()
w.close()