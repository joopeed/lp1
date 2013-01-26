# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

n = int(raw_input())
soma =0
for i in range(n):
	chegada,saida = map(int, raw_input().split())
	if i==0:
		inicio = chegada
	elif i==n-1:
		fim = saida
	soma+= saida-chegada
print (fim-inicio)-soma
		
	
