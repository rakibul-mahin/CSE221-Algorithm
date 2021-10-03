'''
Selection Sort will return an array which is basically sorted
'''

def selection_sort(arr):
    for i in range(len(arr)):
        
        minPos = i
        for j in range(i+1, len(arr)):
            if int(arr[minPos]) > int(arr[j]):
                minPos = j
        #This is the swapping part
        arr[i], arr[minPos] = arr[minPos], arr[i]
        
    return arr

with open('input2.txt','r') as input_file:
    line_array = input_file.read().splitlines()
    
    '''
    In, n we will have a list in index 0 there will be number of
    elements. In index 1 we will have the number of how many data
    we want to write in our file. Both the elements will be in
    string format.
    '''
    
    n = line_array[0].split(" ")
    data = line_array[1].split(" ")
    
    sorted_arr = selection_sort(data)
    
    with open('output2.txt','w') as write_file:
        [write_file.write(sorted_arr[i]+" ") for i in range(int(n[1]))]  