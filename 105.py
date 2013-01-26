# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def conta_palavras(j, palavras):
	conta=0
	palavras = palavras.split(":")
	for i in palavras:
		if len(i)>=j:
			conta+=1
	return conta
	
assert conta_palavras(5, "zero:um:dois:tres:quatro:cinco") == 2
