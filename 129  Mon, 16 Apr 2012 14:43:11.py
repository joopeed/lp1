# Date: Mon, 16 Apr 2012 14:43:11 +0000
# Question 129
# JOAO PEDRO FERREIRA
# 21211940
# JORGE ABRANTES - Programacao 1 - 2012.1
def zera_negs(m):
        for i in range(len(m)):
                for j in range(len(m[i])):
                        if m[i][j] < 0:
                                m[i][j] = 0
