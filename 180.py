def colegas_de_sala(salasprofs, professor):
	resu = []
	for prof, sala in salasprofs.items():
		if salasprofs[professor] == sala and professor!=prof:
			resu.append(prof)
	return resu


salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204
}
assert set(colegas_de_sala(salasprofs, 'Franklin')) == set(['Tiago', 'Eliane'])
assert set(colegas_de_sala(salasprofs, 'Adalberto')) == set([])	
