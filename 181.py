def cria_mapa(lista):
	digitos = {}
	for conta in lista:
		if digitos.has_key(conta%11):
			digitos[conta%11].append(conta)
		else:
			digitos[conta%11] = [conta]
	return digitos

contas = [5521, 5243, 5680, 4209, 1499]
assert cria_mapa(contas) == {3: [1499], 4: [5680], 7: [5243, 4209], 10: [5521]}

