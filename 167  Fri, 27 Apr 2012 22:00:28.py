# Date: Fri, 27 Apr 2012 22:00:28 +0000
# Question 167
# JOAO PEDRO FERREIRA DE MELO
# 21211940
def eh_quadrado_magico(quad):
	diagonal1 = 0
	diagonal2 = 0
	linhas =[]
	colunas = {}
	for i in range(len(quad)):
		linha =0
		for j in range(len(quad[0])):
			for ii in range(len(quad)):
				for jj in range(len(quad[0])):
					if quad[i][j]==quad[ii][jj] and i!=11 and j!=jj:
						return False
		=09
			if i==j:
				diagonal1+=quad[i][j]
			if i+j==len(quad)-1:
				diagonal2+=quad[i][j]
			linha+=quad[i][j]
			if colunas.has_key(j):
				colunas[j]+=quad[i][j]
			else:
				colunas[j]=quad[i][j]
		linhas.append(linha)
	ultima =0
	for i in range(len(linhas)):
		if i>0:
			if ultima!=linhas[i]:
				return False
		ultima=linhas[i]
	aux = 0
	colunas = colunas.values()
	for i in range(len(colunas)):
		if i>0:
			if aux!=colunas[i]:
				return False
		aux=colunas[i]
	if diagonal1==diagonal2==ultima==aux:
		return True
	else:
		return False
