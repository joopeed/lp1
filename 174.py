def alcance_retweet(u, seguidores):
	resu = [0]*len(seguidores)
	for i in range(len(seguidores[u])):
		if seguidores[u][i] == 1:
			resu[i] = 1
			for j in range(len(seguidores[i])):
				if seguidores[i][j] == 1:
					resu[j] = 1
	return resu
M = [[-1,0,0,1,0],
     [0,-1,0,1,0], 
     [0,0,-1,1,1], 
     [1,1,0,-1,0], 
     [0,1,1,0,-1]]
print alcance_retweet(0, M)
print alcance_retweet(4, M)						
