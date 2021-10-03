'''
Best Case is going to be when the array is sorted by default.
In this best case, time complexity will be less.
If I analyze my code below I will see that array[i] will never
be greater than array[i+1] when my array is already sorted,
therefore run will never be 'True' and thus the main while loop
is not going to run and my time complexity will be n.
'''
def bubble_sort(array):
    run = True
    iteration_count = 0
    array_length = len(array)
    
    while run:
        run = False
        for i in range(array_length - iteration_count - 1):
            if array[i] > array[i+1]:
                run = True
                array[i], array[i+1] = array[i+1], array[i]
                
        iteration_count += 1

    return array

with open('input1.txt','r') as read_file:
    data = read_file.read().splitlines()[1].split()
    sorted_arr = bubble_sort(data)
    
    with open('output1.txt','w') as write_file:
        [write_file.write(i+" ") for i in sorted_arr]
            