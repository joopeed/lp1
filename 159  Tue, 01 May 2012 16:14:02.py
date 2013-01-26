# Date: Tue, 01 May 2012 16:14:02 +0000
# Question 159
# Joao Pedro Ferreira de Melo
# 21211940=20

def mult_linha(n, escalar, m):
        if n >= len(m) or n <0:
                return False
        for i in range(len(m[n])):
                m[n][i]*=escalar
        return True
