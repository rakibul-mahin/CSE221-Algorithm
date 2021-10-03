r = open('input1.txt', 'r')
w = open('output1temp.txt', 'w')

my_data = []

for i in r.readlines():
    my_data.append(i)

clean_data = []
for i in my_data:
    temp = i.replace('\n','')
    clean_data.append(temp)
    
num = int(clean_data.pop(0))

final_data = []
for i in clean_data:
    final_data.append(i.split())

p = 1
for i in range(num):
    min_idx = i #index
    for j in range(i+1, num):
        if int(final_data[min_idx][p]) > int(final_data[j][p]):
            min_idx = j
    
    final_data[i], final_data[min_idx] = final_data[min_idx], final_data[i]
'''
p = 1
for i in range(num):
    swapped = False
    for j in range(0, num-i-1):
        if int(final_data[j][p]) > int(final_data[j+1][p]):
            final_data[j], final_data[j+1] = final_data[j+1], final_data[j]
            swapped = True
            
    if swapped == False:
        break
'''

output_array = []

output_array.append(final_data.pop(0))
total = 1
c_end = output_array[0][1]

for i in final_data:
    s = int(i[0])
    e = int(i[1])
    
    if int(c_end) <= s:
        output_array.append(i)
        total += 1
        c_end = e
        
w.write(str(total)+"\n")
for i in output_array:
    w.write(i[0])
    w.write(" ")
    w.write(i[1])
    w.write('\n')

r.close()
w.close()