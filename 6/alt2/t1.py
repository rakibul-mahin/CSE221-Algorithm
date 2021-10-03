def LCS(x, y):
    m = len(x) + 1
    n = len(y) + 1
   
    # Initialize checker and tracker matrix with deafult values  
    c = [ [0] * (n) for i in range(m) ]
    t = [ [None] * (n) for i in range(m) ]
    
    # Update the values of  row and coluumn for checker and tracker matrix
    
    i = 1
    while i < m:
        c[i][0] = 0
        t[i][0] = None
        i += 1

    j = 1
    while j < n:
        c[0][j] = 0
        t[0][j] = None
        j += 1
        
    i = 1
    j = 1
    
    print(n, m)
    
    while i <= m-1:
        while j <= n-1:
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                t[i][j] = "diagonal"
                j += 1
            else:
                if c[i-1][j] > c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    t[i][j] = "up"
                    j += 1
                elif c[i][j-1] > c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    t[i][j] = "left"
                    j += 1
                elif c[i][j-1] == c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    t[i][j] = "up"
                    j += 1
        
        i += 1
        j = 1
                            
    return ( c, t )   

# Backtracing 
def tracker(t):
    marker = t[len(t) - 1][len(t) - 1]
    i = len(t) - 1
    j = len(t) - 1
    lcs_sequence = []

    while marker != None:
        if marker == "diagonal":
            lcs_sequence += [i]
            marker = t[i - 1][j - 1]
            i -= 1
            j -= 1
        
        elif marker == "up":
            marker = t[i - 1][j]
            i -= 1
        
        elif marker == "left":
            marker = t[i][j - 1]
            j -= 1
        
    return lcs_sequence
#------------------------ Tester Code -----------------------------------
fr = open("input1.txt", "r")
fw = open("output1.txt", "w")

zone_count = fr.readline()
n = int(zone_count)
x = fr.readline().replace("\n", "")
y = fr.readline().replace("\n", "")

y_tracker =  [
            [None, None],
            ["Yasnaya", "Y"],
            ["Pochinki", "P"],
            ["School", "S"],
            ["Rozhok", "R"],
            ["Farm", "F"],
            ["Mylta", "M"],
            ["Shelter", "H"],
            ["Prison", "I"],
       ]        

data = LCS(x, y)
#c = data[0]
t = data[1]

sequence = tracker(t)

for count in sequence[::-1]:
    fw.write(str(y_tracker[count][0]) + " ")


# Correctness percentage 
correctness = (len(sequence) * 100) // n
fw.write("\nCorrectness of prediction: " + str(correctness) + "%")
# File close
fr.close()
fw.close()