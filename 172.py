def inverte3a3(palavra):
	resu = ""
	for i in range(len(palavra)/3,-1,-1):
		resu+=palavra[i*3:i*3+3]
	return resu

print inverte3a3("meusolnaotemcor")
