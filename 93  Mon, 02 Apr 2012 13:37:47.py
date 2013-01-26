# Date: Mon, 02 Apr 2012 13:37:47 +0000
# Question 93
# JOAO PEDRO FERREIRA
# 21211940
def conta_coincidencias(lista1,lista2):
        conta=0
        if len(lista1)>=len(lista2):
                t = len(lista2)
        else:
                t = len(lista1)
        for i in range(t):
                if lista1[i]==lista2[i]:
                        conta+=1=20
        return conta

assert conta_coincidencias([1,2,3,4], [5,6,7]) == 0=20
   =20
assert conta_coincidencias([1,2,3,4], [2,3,3,4]) == 2

assert conta_coincidencias([1,2],[1,3]) == 1
   =20
lista1=map(int, raw_input().split())
lista2=map(int, raw_input().split())
print conta_coincidencias(lista1,lista2)
