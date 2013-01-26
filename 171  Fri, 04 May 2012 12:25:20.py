# Date: Fri, 04 May 2012 12:25:20 +0000
# Question 171
# coding: utf-8=2# Jo=E3o Pedro Le=F4ncio
# Matricula: 21211940
# Programa=E7=E3o 1 - UFCG 2012.1

while True:
	# L=EA as partidas=20
	partidas = map(int, raw_input().split())
	# Se a o usuario digitar 0, encerra
	if partidas == [0]: break
=09
	# Guarda a soma inicial
	soma = sum(partidas)
=09
	# Se for divisivel pelo numero de jogadores, significa que para no ultimo
	if soma%len(partidas)==0:
	=09
		print len(partidas)
	# Se n=E3o for, significa que para no resto da divisao
	else:
	=09
		print soma%len(partidas)
