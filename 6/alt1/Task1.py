def find_max(num1, num2):
    max_num = num1 if num1 > num2 else num2
    return max_num
    
def LCS(str1, str2, num_of_zones):
    n, m = len(str1), len(str2)
    array = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            if str1[i] == str2[j]:
                array[i+1][j+1] = array[i][j] + 1
            else:
                array[i+1][j+1] = find_max(array[i][j+1], array[i+1][j])
                
    length = array[-1][-1]
    
    output = ''
    i = m
    j = n
        
    while i > 0 or j > 0:
        if str1[i-1] == str2[j-1] and array[i-1][j-1] + 1 == array[i][j]:
            output += str1[i-1]
            i -= 1
            j -= 1
        elif str1[i-1] != str2[j-1] and array[i-1][j] > array[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    output = output[-1::-1]
    
    correctness = (length * 100) // num_of_zones
            
    return output, correctness

with open('input1.txt', 'r') as input1:
    with open('output1.txt', 'w') as output1:
        all_lines = input1.read().splitlines()
        total, str1, str2 = map(str, all_lines)
        total = int(total)
        output, correctness = LCS(str1,str2,total)
        
        pubgm = {
            "Y": "Yasnaya",
            "P": "Pochinki",
            "S": "School",
            "R": "Rozhok",
            "F": "Farm",
            "M": "Mylta",
            "H": "Shelter",
            "I": "Prison"
        }
        
        length = len(output)
        count = 1
        for i in output:
            if i in pubgm and count == length:
                output1.write(str(pubgm[i])+"\n")
            elif i in pubgm:
                output1.write(str(pubgm[i])+" ")
                count += 1
                
        output1.write("Correctness of prediction: "+str(correctness)+"%")