# Date: Mon, 02 Apr 2012 14:44:56 +0000
# Question 95
# JOAO PEDRO LEONCI# 21211940
def z_inicial(lista):
        conta=0
        for i in lista:
                if i[0].lower() =="z":
                        conta+=1
        if conta!=0:
                return conta
        else:
                return 0
lista = raw_input().split()
print z_inicial(lista)
