# Date: Tue, 01 May 2012 16:19:55 +0000
# Question 162
# Joao Pedro Ferreira de Melo
# 21211940=20
def matriz_coincidencia(m1,m2):
        m = [len(m1[0])*[0] for i in range(len(m1))]
        for i in range(len(m1)):
                for j in range(len(m1[0])):
                        if m1[i][j] == m2[i][j]:
                                m[i][j] = m1[i][j]
        return m
