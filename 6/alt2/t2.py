def lcs3(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    L = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    L[i+1][j+1][k+1] = L[i][j][k] + 1
                else:
                    L[i+1][j+1][k+1] = max(L[i+1][j+1][k],L[i][j+1][k+1],L[i+1][j][k+1])

    lcs = ""
    while m > 0 and l > 0 and n > 0:
        step = L[m][l][n]
        if step == L[m-1][l][n]:
            m -= 1
        elif step == L[m][l-1][n]:
            l -= 1
        elif step == L[m][l][n-1]:
            n -= 1
        else:
            lcs += str(a[m-1])
            m -= 1
            l -= 1
            n -= 1

    return len(lcs[::-1])
    
r = open('input2.txt', 'r')
w = open('output2.txt', 'w')

text = []

for i in r:
    text.append(i.replace('\n',''))
    
w1 = text[0]
w2 = text[1]
w3 = text[2]

length = lcs3(w1, w2, w3)

w.write(str(length))

r.close()
w.close()