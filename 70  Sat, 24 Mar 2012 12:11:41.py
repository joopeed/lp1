# Date: Sat, 24 Mar 2012 12:11:41 +0000
# Question 70
# JOAO PEDRO FERREIRA
# 21211940
num = map(int, raw_input().split())
nomes = raw_input().split()
maior = 0
indice = 0
for i in range(len(num)):
        if num[i] > maior:
                maior = num[i]
                indice = i
print nomes[indice], num[indice]
