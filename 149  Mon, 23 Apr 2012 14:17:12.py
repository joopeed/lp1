# Date: Mon, 23 Apr 2012 14:17:12 +0000
# Question 149
# JOAO PEDRO FERREIRA -21211940
## PROGRAMACAO 1 - UFCG 2012.1 - JORGE ABRANTES
### 149

texto = raw_input().lower()
ocorreu = {}
for i in texto:
        if i in ocorreu:
                ocorreu[i] += 1
        else:
                ocorreu[i] =1
maior=0
for i in range(len(ocorreu.values())):
        if ocorreu.values()[i] > ocorreu.values()[maior]:
                maior = i
print ocorreu.keys()[maior],ocorreu.values()[maior]

