# Date: Mon, 02 Apr 2012 13:47:08 +0000
# Question 94
# JOAO PEDRO FERREIRA
# 21211940
def encontra_menores(num,lista):
        ok = -1
        for i in lista:
                if i < num:
                        ok = i
                        break
        return ok
lista = map(int, raw_input().split())
num = int(raw_input())
print encontra_menores(num, lista)
