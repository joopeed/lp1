def senha(cadastro, user):
	for chave,valor in cadastro.items():
		if user in valor:
			return chave
	return -1

splab = {1313:['Franklin', 'Jorge'], 1226:['Eliane', 'Dalton'], 1507:['Wilkerson'] }
assert senha(splab, 'Franklin') == 1313
assert senha(splab, 'Matheus') == -1
