def find_max(num1, num2):
    max_num = num1 if num1 > num2 else num2
    return max_num
    
def LCS(str1, str2, str3):
    n, m, l = len(str1), len(str2), len(str3)

    array = [[[0 for _ in range(l)] for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(l):
                array[i][j][k] = 0
                if str1[i] == str2[j] and str1[i] == str3[k]:
                    if  i > 0 and j > 0 and k > 0:
                        val = array[i-1][j-1][k-1] + 1
                    else:
                        val = 0 + 1
                    
                    array[i][j][k] = val
                    
                else:
                    if i > 0:
                        comp1 = array[i-1][j][k]
                    else:
                        comp1 = 0
                        
                    if j > 0:
                        comp2 = array[i][j-1][k]
                    else:
                        comp2 = 0
                        
                    if k > 0:
                        comp3 = array[i][j][k-1]
                    else:
                        comp3 = 0
                        
                    array[i][j][k] = find_max(find_max(comp1, comp2), comp3)
                    
    return array[n-1][m-1][l-1]                        
        
with open('input2.txt', 'r') as input2:
    with open('output2.txt', 'w') as output2:
        all_lines = input2.read().splitlines()
        str1, str2, str3 = map(str, all_lines)
        
        length = LCS(str1, str2, str3)
        output2.write(str(length))