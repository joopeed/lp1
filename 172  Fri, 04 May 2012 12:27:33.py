# Date: Fri, 04 May 2012 12:27:33 +0000
# Question 172
# coding: utf-8=2# Jo=E3o Pedro Le=F4ncio
# Matricula: 21211940
# Programa=E7=E3o 1 - UFCG 2012.1

def inverte3a3(s):
=09
	invertida = list(s[::-1])
	# inverte a string e transforma em lista pra poder manipul=E1-la

	for i in range(1,len(s),3):
		invertida[i-1],invertida[i+1] = invertida[i+1],invertida[i-1]
	# inverte as substrings de 3 em 3
=09
	return "".join(invertida) # retorna em forma string

