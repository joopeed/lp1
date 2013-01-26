# Date: Fri, 20 Apr 2012 22:49:41 +0000
# Question 137
# Joao Pedro Ferreira - 21211940
# Programacao I -  Jorge Abrantes 2012.1
def zera_diagonal(m):
        for i in range(len(m)):
                for j in range(len(m[0])):
                        if  i==j:
                                m[i][j] = 0
