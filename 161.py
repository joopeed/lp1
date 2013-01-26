def movimentos_diagonais(lab):
	conta=0 
	for i in range(len(lab)): 
		for j in range(len(lab[0])): 
			if lab[i][j]=='*': 
				if i+1 < len(lab) and j+1 < len(lab[0]): 
					if lab[i+1][j+1]==" ":
						conta+=1 
				if i-1 >=0 and j-1 >=0: 
					if lab[i-1][j-1]==" ": 
						conta+=1 
				if i-1 >=0 and j+1 < len(lab[0]): 
					if lab[i-1][j+1]==" ": 
						conta+=1 
				if i+1 < len(lab) and j-1 >=0: 
					if lab[i+1][j-1]==" ": 
						conta+=1 
	return conta
