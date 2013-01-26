# Date: Fri, 04 May 2012 12:28:52 +0000
# Question 174
# coding: utf-8=2# Jo=E3o Pedro Le=F4ncio
# Matricula: 21211940
# Programa=E7=E3o 1 - UFCG 2012.1

def alcance_retweet(u, seguidores):

	# gera uma lista vazia pra alocar o alcance
	alcance = [0]*len(seguidores)
=09
	# percorrer e verifica quem sao os seguidores de u=09
	for i in range(len(seguidores[u])):

		if seguidores[u][i] == 1:=20
			# adiciona o proprio seguidor
			alcance[i] = 1

			# percorrer e verifica os seguidores do seguidor
			for j in range(len(seguidores[i])):

				if seguidores[i][j] == 1:

					# adiciona o seguidor do seguidor
					alcance[j] = 1
=09
	return alcance
