def matriz_coincidencia(m1,m2):
	m = [len(m1[0])*[0] for i in range(len(m1))]
	for i in range(len(m1)):
		for j in range(len(m1[0])):
			if m1[i][j] == m2[i][j]:
				m[i][j] = m1[i][j]
	return m

M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M2= [[10, 11, 12],
     [13, 14, 15],
     [ 7,  8,  9]]

M3= [[ 1,  2,  3],
     [13, 14, 15],
     [16, 17, 18]]
   
assert matriz_coincidencia(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]
assert matriz_coincidencia(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]
