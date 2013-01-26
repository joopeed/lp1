# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def conta_dias(dia, mes, ano):
	soma = 0
	for i in range(1,mes+1):
		if mes!=i:
			if i in [1,3,5,7,8,10,12]:
				soma+=31
			elif i ==2:
				if ano%400==0 or(ano%4==0 and not(ano%100==0)):
					soma+=29
				else:
					soma+=28
			else:
				soma+=30
	soma+=dia
	return soma

assert conta_dias(10, 1, 2000) == 10

assert conta_dias(20, 2, 2011) == 51

assert conta_dias(31, 12, 2011) == 365
		
