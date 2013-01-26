# Date: Wed, 26 Sep 2012 23:19:18 +0000
# Question 188
#JOAO PEDRO LEONCIO -  21211940
# 2012.1 - JORGE ABRANTES

def tem123plus(lista):
        ok = [-1,-1,-1]
        pos = -1
        resu = 0
        for i in range(len(lista)):
                if lista[i]==1 and ok[0]==-1:
                        ok[0] =1
                        pos = i
                if lista[i]==2 and ok[0]!=-1:
                        ok[1] =1
                if lista[i]==3 and ok[1]!=-1:
                        ok[2] =1
        for oks in ok:
                if oks>0:
                        resu+=1
        if resu==3:
                return pos
        else:
                return -1
