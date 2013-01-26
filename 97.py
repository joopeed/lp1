# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

num = int(raw_input())
lista = map(int, raw_input().split())
indice=-1
conta=0

for i in range(len(lista)):
	if lista[i]==num:
		conta+=1
		if conta>1:
			indice=i
print indice	
