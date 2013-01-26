# Date: Fri, 04 May 2012 12:28:14 +0000
# Question 173
# coding: utf-8=2# Jo=E3o Pedro Le=F4ncio
# Matricula: 21211940
# Programa=E7=E3o 1 - UFCG 2012.1

def pagamento_IPVA(veiculos, mes):
=09
	# Os veiculos que ter=E3o que pagar no mes recebido ficarao nesta lista
	veiculosdomes = []=09
	=09
	# Se o m=EAs n=E3o for 10, ser=E1 um digito normal convertido em string pa=
ra ser comparado
	if mes != 10:=20
		mescomparativo = str(mes)
	# Se for 10, ser=E1 substituido por 0
	else:
		mescomparativo = "0"=09

	# Percorre de tr=E1s para frente para nao haver conflito com o pop
	for i in range(len(veiculos)-1,-1,-1):
		if veiculos[i][-1] == mescomparativo:
			veiculosdomes.append(veiculos[i])
			veiculos.pop(i)
=09
	return veiculosdomes[::-1] # Como percorri de tr=E1s para frente, a ordem =
sai invertida, ent=E3o assim inverto novamente
