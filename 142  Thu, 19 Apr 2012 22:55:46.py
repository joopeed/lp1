# Date: Thu, 19 Apr 2012 22:55:46 +0000
# Question 142
# coding: utf-8=2# Jo=E3o Pedro Ferreira=20
# 21211940 - Programa=E7=E3o 1 - UFCG=20
def movimentos_possiveis(labirinto):=20
	conta=0=20
	for i in range(len(labirinto)):=20
		for j in range(len(labirinto[i])):=20
			if labirinto[i][j] == '*':=20
				if i-1 >=0:
					if labirinto[i-1][j]== ' ':=20
						conta+=1=20
				if i+1 < len(labirinto):
					if labirinto[i+1][j]== ' ':=20
						conta+=1=20
				if j-1 >=0:
					if labirinto[i][j-1]== ' ':=20
						conta+=1=20
				if j+1 < len(labirinto[0]):
					if labirinto[i][j+1]== ' ':=20
						conta+=1=20
	return conta
