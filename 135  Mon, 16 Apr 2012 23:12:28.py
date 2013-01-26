# Date: Mon, 16 Apr 2012 23:12:28 +0000
# Question 135
def somacols(m)        colunas = []
        for j in range(len(m[0])):
                coluna =0
                for i in range(len(m)):
                   coluna+=m[i][j]
                colunas.append(coluna)
        return colunas
