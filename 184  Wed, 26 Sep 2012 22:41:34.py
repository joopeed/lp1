# Date: Wed, 26 Sep 2012 22:41:34 +0000
# Question 184
#JOAO PEDRO LEONCIO -  21211940
# 2012.1 - JORGE ABRANTES

def dominante(lista):
        dic = {}
        resu = -1
        for i in lista:
                if i in dic:
                        dic[i]+=1
                else:
                        dic[i]=1
        for chave, valor in dic.items():
                if valor>len(lista)/2:
                        resu = chave
        return resu
