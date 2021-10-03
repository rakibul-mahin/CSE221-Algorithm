'''
This is Insertion Sort, this will sort the id_arr with respect
to mark_err. For example if one mark is greater and going to
be swapped, then both the mark and its corresponding ID in
id_arr will also be swapped.
'''

def insertion_sort(mark_arr, id_arr):
    n = len(mark_arr)
    
    for i in range(n-1):
        #This temporarily stores marks
        temp = mark_arr[i+1]
        #This temporarily stores id
        temp2 = id_arr[i+1]
        j = i
        
        while(j >= 0):
            if mark_arr[j] > temp:
                mark_arr[j+1] = mark_arr[j]
                id_arr[j+1] = id_arr[j]
            else:
                break
        
            j -= 1
        
        mark_arr[j+1] = temp
        id_arr[j+1] = temp2
    
    return id_arr
    
def get_output(id_arr):
    with open('output3.txt', 'w') as output3_file:
        [output3_file.write(id_arr[i]+" ") for i in range(-1, -1*n-1, -1)]
            

with open("input3.txt","r") as input_file:
    lines_in_array = input_file.read().splitlines()
    n = int(lines_in_array[0])
    id_array = lines_in_array[1].split(" ")
    marks_array = lines_in_array[2].split(" ")
    
    id_array = insertion_sort(marks_array, id_array)
    get_output(id_array)