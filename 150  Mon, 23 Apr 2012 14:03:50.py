# Date: Mon, 23 Apr 2012 14:03:50 +0000
# Question 150
# JOAO PEDRO FERREIRA -21211940
## PROGRAMACAO 1 - UFCG 2012.1 - JORGE ABRANTES
### 150

def turma_pratica(alocacao,t):
        conta = 0
        for i in alocacao.values():
                if i[1] == t:
                        conta+=1
        return conta
