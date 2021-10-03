r = open('input2.txt', 'r')
w = open('output2.txt', 'w')

my_data = []

for i in r.readlines():
    my_data.append(i)

clean_data = []
for i in my_data:
    temp = i.replace('\n','')
    clean_data.append(temp)


non_assignment_data = clean_data.pop(0)
num, stud = non_assignment_data.split()

num = int(num)
stud = int(stud)

final_data = []
for i in clean_data:
    final_data.append(i.split())

p = 1
for i in range(num):
    swapped = False
    for j in range(0, num-i-1):
        if int(final_data[j][p]) > int(final_data[j+1][p]):
            final_data[j], final_data[j+1] = final_data[j+1], final_data[j]
            swapped = True
            
    if swapped == False:
        break

total = 0
free_time = []
for i in range(stud):
    free_time.append(0)

c = 0
for i in range(stud):
    total += 1
    temp = final_data.pop(0)
    free_time[c] = temp[1]
    c += 1
    
for i in final_data:
    s = int(i[0])
    e = int(i[1])
    
    for j in range(len(free_time)):
        if int(free_time[j]) < s:
            total += 1
            free_time[j] = e
            break
        
w.write(str(total)+"\n")

r.close()
w.close()