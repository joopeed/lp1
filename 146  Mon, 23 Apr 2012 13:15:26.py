# Date: Mon, 23 Apr 2012 13:15:26 +0000
# Question 146
# JOAO PEDRO FERREIRA - 21211940
## PROGRAMACAO1 - UFCG 2012.1 - JORGE ABRANTES
### QUESTAO 146

def num_espacos(labirinto):
        conta=0
        for i in range(len(labirinto)):
                for j in range(len(labirinto[0])):
                        if labirinto[i][j] in "* ":
                                conta+=1
        return conta
