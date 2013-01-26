# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def indices_de_idosos(fila):
	idosos = []
	for i in range(len(fila)):	
		if fila[i] > 60:
			idosos.append(i)
	return idosos

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]

assert indices_de_idosos(fila) == [2, 3, 9, 10]	
