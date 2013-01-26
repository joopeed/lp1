# Date: Wed, 26 Sep 2012 23:03:31 +0000
# Question 187
#JOAO PEDRO LEONCIO -  21211940
# 2012.1 - JORGE ABRANTES

def tem123(lista):
        resu = -1
        for i in range(len(lista)-2):
                if lista[i]==1 and lista[i+1]==2 and lista[i+2]==
=3:
                        resu = i
        return resu
