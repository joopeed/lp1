def soma_matriz_interna(m, inicio, fim):
	soma =0
	for i in range(inicio[0],fim[0]+1):
		for j in range(inicio[1], fim[1]+1):
			soma+= m[i][j]
	return soma
m = [[1,2,3],[4,5,6],[7,8,9]]
print soma_matriz_interna(m, (1,1),(2,2))
