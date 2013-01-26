# Date: Fri, 30 Mar 2012 22:51:17 +0000
# Question 92
# JOAO PEDRO LEONCI# 21211940
nomes = raw_input().split()
idades = map(int, raw_input().split())
for i in range(len(idades)):
        if idades[i] >=18:
                print nomes[i]
