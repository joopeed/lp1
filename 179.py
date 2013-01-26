def indices_de_idosos(fila):
	resu =[]
	for i in range(len(fila)):
		if fila[i] >60:
			resu.append(i)
	return resu

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
assert indices_de_idosos(fila) == [2, 3, 9, 10]


