# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def maior_palavra(lista):
	maior = lista[0]
	for i in lista:
		if len(i) >= len(maior):
			maior = i
	return maior;
lista1 = ["palavra", "exemplo", "computador", "mouse"]

lista2 = ["outra", "palavra", "como", "exemplo", "mouse"]

assert maior_palavra(lista1) == "computador"

assert maior_palavra(lista2) in ["palavra", "exemplo"]
