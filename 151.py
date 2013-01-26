def procura_elemento(m,ele):
	result = (-1,-1)
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j] == ele:
				result = (i,j)
	return result


m = [[1, 2],[ 3, 4], [5,6]]
assert procura_elemento(m,6) == (2,1)
assert procura_elemento(m,7) == (-1,-1)


