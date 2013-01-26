# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def prevogais(palavra):
	lista =[]
	for i in range(len(palavra)-1):
		if palavra[i+1] in "AEIOUaeiou":
			lista.append(palavra[i])
	return lista

assert prevogais("exemplo") == ['x', 'l']

assert prevogais("hiato") == ['h', 'i', 't']
