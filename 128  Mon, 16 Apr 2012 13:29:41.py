# Date: Mon, 16 Apr 2012 13:29:41 +0000
# Question 128
#coding: utf-# JOAO PEDRO FERREIRA
# PROG1 - UFCG - 2012.1 - Jorge Abrantes

def elimina_menores(alunos):
	conta=0
	for i in range(len(alunos)-1,-1,-1):
		if alunos[i][1] <18:
			alunos.pop(i)
			conta+=1
	return conta
