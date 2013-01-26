# Date: Thu, 26 Apr 2012 11:28:05 +0000
# Question 161
# JOAO PEDRO LEONCIO - 21211940
# PROGRAMACAO I - UFCG 201.1 -JORGE ABRANTES

def movimentos_diagonais(lab):
        conta=0
        for i in range(len(lab)):
                for j in range(len(lab[0])):
                        if lab[i][j]=='*':
                                if i+1 < len(lab) and j+1 < len(lab[0=
]):
                                        if lab[i+1][j+1]==" "=
:
                                                conta+=1
                                if i-1 >=0 and j-1 >=0:
                                        if lab[i-1][j-1]==" "=
:
                                                conta+=1
                                if i-1 >=0 and j+1 < len(lab[0]):
                                        if lab[i-1][j+1]==" "=
:
                                                conta+=1
                                if i+1 < len(lab) and j-1 >=0:
                                        if lab[i+1][j-1]==" "=
:
                                                conta+=1
        return conta
