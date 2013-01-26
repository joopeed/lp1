# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

dia = int(raw_input())
mes = int(raw_input())
ano = int(raw_input())

if dia not in [31,30,28]:
	dia+=01
else:
	if dia==31 and mes in [1,3,5,7,8,10]:
		dia =01
		mes +=01
	elif dia==28 and mes==2:
		dia=01
		mes+=01
	elif dia==30:
		dia=01
		mes+=01
	elif dia==31 and mes==12:
		dia=01
		mes=01
		ano+=01
	else:
		dia+=01
print "%02d"%dia 
print "%02d"%mes
print ano
		
