# Date: Sat, 06 Oct 2012 01:01:52 +0000
# Question 181
# JOAO PEDRO LEONCIO - 21211940=20
# UFCG 2012.1 - JORGE ABRANTES=20
def cria_mapa(lista):=20
	digitos = {}
	for conta in lista:=20
		if digitos.has_key(conta%11):=20
			digitos[conta%11].append(conta)=20
		else:=20
			digitos[conta%11] = [conta]=20
	return digitos
