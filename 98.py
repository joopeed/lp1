# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

dado = map(float, raw_input().split())
hora = raw_input().split()
maior = dado[0]
menor = dado[0]
indicemaior = 0
indicemenor = 0

for i in range(len(dado)):
	if dado[i] > maior:
		maior = dado[i]
		indicemaior = i
	if dado[i] < menor:
		menor = dado[i]
		indicemenor = i
print "Min:",hora[indicemenor],"%.2f"% dado[indicemenor]
print "Max:",hora[indicemaior],"%.2f"% dado[indicemaior]

