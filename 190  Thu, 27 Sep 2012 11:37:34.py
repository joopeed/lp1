# Date: Thu, 27 Sep 2012 11:37:34 +0000
# Question 190
# JOAO PEDRO LEONCIO - 21211940
# PROG1 - 2012.1 - JORGE ABRANTES

def sequencia_caras(lista):
        k = 0
        total, maior = 0, 0
        while k < len(lista):
                if lista[k] == 0:
                        total = 0
                else:
                        total+=1
                        maior = max(maior, total)

                k+=1
        return maior
