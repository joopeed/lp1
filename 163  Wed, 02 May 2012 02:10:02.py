# Date: Wed, 02 May 2012 02:10:02 +0000
# Question 163
# JOAO PEDRO FERREIRA DE MELO LEONCIO - 21211940
# PROGRAMACAO I - UFCG - 2012.1

def matriz_menor(m1,m2):
        matriz = []
        for i in range(len(m1)):
                linha = []
                for j in range(len(m1[0])):
                        if m1[i][j]<m2[i][j]:
                                linha.append(m1[i][j])
                        else:
                                linha.append(m2[i][j])
                matriz.append(linha)

        return matriz
