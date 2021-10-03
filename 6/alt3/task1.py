def lcs(x,y):
    m=len(x)
    n=len(y)

    L=[[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j]=0
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    
    index = L[m][n]
    seq = [""] * (index + 1)
    seq[index] = ""
    
    i, j = m, n
    
    while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                seq[index-1] = x[i-1]
                i = i - 1
                j = j - 1
                index -= 1
            elif L[i][j-1] < L[i-1][j]:
                i = i - 1
            else:
                j = j - 1
                
    seq_str=''.join(seq[:-1])
    return seq_str





r = open('input1.txt', 'r')
w = open('output1.txt', 'w')



data = []

for i in r:
    data.append(i.replace('\n',''))

total = int(data[0])
word1 = data[1]
word2 = data[2]

my_dict = {
            "Y": "Yasnaya",
            "P": "Pochinki",
            "S": "School",
            "R": "Rozhok",
            "F": "Farm",
            "M": "Mylta",
            "H": "Shelter",
            "I": "Prison"
}

seq = lcs(word1, word2)

for i in seq:
    if i in my_dict.keys():
        w.write(my_dict[i]+" ")
w.write("\nCorrectness of Prediction: "+str(len(seq)* 100 // total)+"%")        
        

r.close()
w.close()