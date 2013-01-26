# Date: Mon, 23 Apr 2012 14:20:39 +0000
# Question 148
# JOAO PEDRO FERREIRA -21211940
## PROGRAMACAO 1 - UFCG 2012.1 - JORGE ABRANTES
### 148

def devedores(contas):
        conta = 0
        for i in range(len(contas.values())):
                if contas.values()[i] <0:
                        conta+=1
        return conta
