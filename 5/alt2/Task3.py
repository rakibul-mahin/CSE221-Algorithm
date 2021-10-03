r = open('input3.txt', 'r')
w = open('output3.txt', 'w')

data = []

for i in r:
    data.append(i.replace('\n',''))
    
tasks = data[1].split()
call = data[2]

tasks.sort()

output = ""
jack = []
jill = []

timeJ = 0
timej = 0

leastPointer = 0

for i in call:
    if i == 'J':
        least = tasks[leastPointer]
        jack.append(least)
        timeJ += int(least)
        output += least
        leastPointer += 1
    elif i == 'j':
        p = 0
        temp = jack
        temp.sort(reverse=True)
        broMax = temp[p]
        check = True
        
        while check:
            if broMax not in jill:
                jill.append(broMax)
                timej += int(broMax)
                output += broMax
                check = False
            else:
                p+=1
                broMax = temp[p]
        
w.write(output+"\n")
w.write('Jack will work for '+str(timeJ)+" hours\n")
w.write('Jill will work for '+str(timej)+" hours\n")

r.close()
w.close()