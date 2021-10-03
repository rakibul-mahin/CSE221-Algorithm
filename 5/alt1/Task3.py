with open('task3_output.txt', 'w') as output3:
    with open('task3_input.txt', 'r') as input3:
        all_lines = input3.read().splitlines()
        total_tasks = int(all_lines[0])
        call_sequence = all_lines[-1]
        all_lines = all_lines[1:2]
        task_list = all_lines[0].split()
        task_list = list(map(int, task_list))
        
        task_list.sort()
        
        J_hours = 0
        j_hours = 0
        
        J_tasks = []
        j_tasks = []
        
        order = ""
        
        pointer = 0
        
        for i in call_sequence:
            if i == "J":
                selected = task_list.pop(0)
                J_tasks.append(selected)
                J_hours += selected
                order += str(selected)
            elif i == "j":
                selected = J_tasks.pop()
                j_tasks.append(selected)
                j_hours += selected
                order += str(selected)
        
        output3.write(str(order)+"\n")
        output3.write(f'Jack will work for {J_hours} hours\nJill will work for {j_hours} hours')