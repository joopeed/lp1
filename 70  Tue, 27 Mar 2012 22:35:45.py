# Date: Tue, 27 Mar 2012 22:35:45 +0000
# Question 70
# JOAO PEDRO FERREIRA=20
# 21211940=20
num = map(int, raw_input().split())=20
nomes = raw_input().split()=20
maior = 0=20
indice = 0=20
for i in range(len(num)):=20
	if num[i] > maior:=20
		maior = num[i]=20
		indice = i=20
print nomes[indice], num[indice]
