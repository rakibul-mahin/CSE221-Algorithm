r = open('input2.txt', 'r')
w = open('output2.txt', 'w')

data = []

for i in r:
    data.append(i.replace('\n',''))


num = int(data[0][0])
people = int(data[0][2])

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
worker_details = [0] * people
c = 0

for i in range(people):
    final.append(twoD[c])
    worker_details[c] = final[c][1]
    c += 1
    assignment_done += 1

for i in range(people):
    twoD.pop(0)

for i in twoD:
    start = i[0]
    end = i[1]
    
    for j in range(len(worker_details)):
        if worker_details[j] < start:
            assignment_done += 1
            worker_details[j] = end
            break
 
w.write(str(assignment_done))
r.close()
w.close()