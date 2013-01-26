# Date: Mon, 23 Apr 2012 14:24:20 +0000
# Question 147
# JOAO PEDRO FERREIRA -21211940
## PROGRAMACAO 1 - UFCG 2012.1 - JORGE ABRANTES
### 147
def ausentes(livros):
        conta=0
        for i in range(len(livros.values())):
                if livros.values()[i] == 0:
                        conta+=1
        return conta
