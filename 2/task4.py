'''
This is one of the most efficient sorting alogorithm.
This is Divide and Conquer method.
'''

def merge(array, lower, centre, upper):
    n1 = centre - lower + 1
    n2 = upper - centre
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = array[lower + i]
        
    for j in range(0, n2):
        R[j] = array[centre + 1 + j]
        
    i = 0
    j = 0
    k = lower
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        
        k += 1
        
    while  i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1       
        
def mergeSort(array, lower, upper):
    
    if lower < upper:
        mid = (lower + (upper - 1 )) // 2
        
        mergeSort(array, lower, mid)
        mergeSort(array, mid+1, upper)
        merge(array, lower, mid, upper)
    
    #This will create a Output text file
    with open ('output4.txt','w') as write_file:
        for i in array:
            write_file.write(str(i)+" ")
    
#This will read data from a file
with open('input4.txt', 'r') as input_file:
     lines_in_array = input_file.read().splitlines()
     lines_in_array = lines_in_array[1].split(' ')
     
     for i in range(len(lines_in_array)):
         lines_in_array[i] = int(lines_in_array[i])
         
mergeSort(lines_in_array, 0, len(lines_in_array)-1)