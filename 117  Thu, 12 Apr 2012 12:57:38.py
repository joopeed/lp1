# Date: Thu, 12 Apr 2012 12:57:38 +0000
# Question 117
# coding: utf-# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940
def filtra_altera_lista(num, lista):
	for i in range(len(lista)-1,-1,-1):
		if i%num!=0:
			lista.pop(i)
