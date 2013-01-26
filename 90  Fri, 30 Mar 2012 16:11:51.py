# Date: Fri, 30 Mar 2012 16:11:51 +0000
# Question 90
# JOAO PEDRO LEONCI# 21211940
meses=['jan','fev','mar', 'abr', 'mai=
', 'jun', 'jul', 'ago', 'set', 'out=
','nov','dez']
saldo=0
maior=0
maiorzao=0
despesas = map(int, raw_input().split())
for i in range(12):
        saldo+=500
        saldo -= despesas[i]
        if saldo >= maior:
                maior = saldo
                maiorzao = i
print meses[ maiorzao]
