with open('task1_output.txt', 'w') as output1:
    with open('task1_input.txt', 'r') as input1:
        all_lines = input1.read().splitlines()
        total_assignments = int(all_lines[0])
        all_lines = all_lines[1:]
        main_array = []
        
        for i in all_lines:
            temp = i.split()
            temp = list(map(int, temp))
            main_array.append(temp)
            
        main_array.sort(key = lambda x: x[1])
        result = []
        count = 0
        
        start_index = 0
        end_index = 1
        
        result.append(main_array[0])
        count += 1
        end_time = result[0][end_index]
        
        main_array = main_array[1:]
        
        for _, j in enumerate(main_array):
            if j[start_index] >= end_time:
                result.append(j)
                count += 1
                end_time = j[1]
                
        output1.write(str(count)+"\n")
        
        last_result = result.pop()

        for i in result:
            output1.write(str(i[0])+" "+str(i[1])+"\n")
            
        output1.write(str(last_result[0])+" "+str(last_result[1]))