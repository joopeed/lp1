# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def quantos_comeram(n,fila):
	soma=0
	ok=True
	for i in fila:
		if i <=n and ok:
			n-=i
		else:
			soma+=i
			ok=False
	soma = sum(fila)-soma 
	return soma

assert quantos_comeram(12, [10, 10]) == 10

assert quantos_comeram(2, [10, 10]) == 0

assert quantos_comeram(5, [2, 3, 5]) == 5 
