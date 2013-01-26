# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940
def lanchemaispedido(pedidos):
	listaprods = []
	quants =[]
	for i in pedidos:
		ok=0
		for j in listaprods:
			if j==i:
				ok =1
		if ok==0:
			listaprods.append(i)
			quants.append(0)
	for i in range(len(listaprods)):
		for j in pedidos:
			if listaprods[i] ==j:
				quants[i]+=1
	ele = None
	for i in range(len(quants)):
		if quants[i] > (len(pedidos)/2):
			ele = listaprods[i]
	return ele
		

ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']

marcos = ['suco','coxinha','suco','misto','folhado']

assert lanchemaispedido(ines) == 'tapioca'

assert lanchemaispedido(marcos) == None
