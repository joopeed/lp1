def colunas_com_zero(m):
	colunas = {}
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j]==0:
				colunas[j]=1
	return sorted(colunas.keys())

assert colunas_com_zero([[5, 0], [3, 1], [2, -4]]) == [1]
assert colunas_com_zero([[1, 3, 0], [0, 1, 0]]) == [0, 2]
