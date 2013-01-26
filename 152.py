def desempenho(m):
	conta=0
	for i in range(len(m)):
		for j in range(len(m[0])):
			if m[i][j] == 1:
				conta+=1
	return conta


m1 = [[1, 1, 0, 1],
      [1, 1, 0, 0],
      [1, 1, 1, 0]]

m2 = [[0, 1, 0, 1],
      [1, 1, None, 0],
      [1, None, None, None]]

assert desempenho(m1) == 8
assert desempenho(m2) == 5
