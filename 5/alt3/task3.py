r = open('input3.txt', 'r')
w = open('output3.txt', 'w')


my_data = []

for i in r.readlines():
    my_data.append(i)

clean_data = []
for i in my_data:
    temp = i.replace('\n','')
    clean_data.append(temp)

num = int(clean_data[0])
task = clean_data[1].split()
call = clean_data[2]

task.sort()

output = []

J = []
j = []

JT = 0
jT = 0

p = 0

for i in call:
    if i == 'J':
        JTask = task[p]
        J.append(JTask)
        JT += int(JTask)
        output.append(JTask)
        p += 1
    else:
        c = 0
        temp = J
        highTime = temp.pop()
        run = True
        
        while run:
            if highTime not in j:
                j.append(highTime)
                jT += int(highTime)
                output.append(highTime)
                run = False
            else:
                c += 1
                highTime = temp[c]

for i in output:
    w.write(i)

w.write('\n')
w.write('Jack will work for '+str(JT)+" hours\n")
w.write('Jill will work for '+str(jT)+" hours\n")

r.close()
w.close()