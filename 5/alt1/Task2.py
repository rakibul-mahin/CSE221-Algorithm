def compare_time(time_arr, start_time, end_time):
    for i, j in enumerate(time_arr):
        if start_time >= j:
            time_arr[i] = end_time
            return True

with open('task2_output.txt', 'w') as output2:
    with open('task2_input.txt', 'r') as input2:
        all_lines = input2.read().splitlines()
        first_line = all_lines[0:1][0].split()
        total_assignments = int(first_line[0])
        total_people = int(first_line[1])
        all_lines = all_lines[1:]
        
        main_array = []
        
        for i in all_lines:
            temp = i.split()
            temp = list(map(int, temp))
            main_array.append(temp)
            
        main_array.sort(key = lambda x: x[1])
        
        worker_times = [0 for _ in range(total_people)]
        result = []
        pointer = 0
        start_index = 0
        end_index = 1
        count = 0
        
        for _ in range(total_people):
            result.append(main_array[pointer])
            worker_times[pointer] = result[pointer][end_index]
            pointer += 1
        
        count += total_people
        main_array = main_array[total_people:]
        
        for i in main_array:
            if compare_time(worker_times, i[start_index], i[end_index]):
                count += 1
                
        output2.write(str(count))