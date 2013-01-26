# Date: Tue, 17 Apr 2012 23:10:15 +0000
# Question 133
# Joao Pedro Leonci## 21211940
### Programacao 1 - Prof. Jorge Abrantes

def transposta(m):
        matriz = []
        for i in range(len(m[0])):
                linha = []
                for j in range(len(m)):
                        linha.append(m[j][i])
                matriz.append(linha)
        return matriz
ma = [[1,2,3],[4,5,6],[7,8,9]]
print transposta(ma)
