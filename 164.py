def constroi_matriz(m,n,valores):
	matriz = []
	for i in range(m):
		linha =[]
		for j in range(n*i,n*i+n):
			print j, n*i, n*i+n, m
			linha.append(valores[j])
		matriz.append(linha)
	return matriz

valores = [1,2,3,4,5,6,7,8]

assert constroi_matriz(2, 4, valores) == [[1,2,3,4], [5,6,7,8]]

assert valores == [1,2,3,4,5,6,7,8]
