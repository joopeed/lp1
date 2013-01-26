def dominante(lista):
	dic = {}
	resu = -1
	for i in lista:
		if i in dic:
			dic[i]+=1
		else:
			dic[i]=1
	for chave, valor in dic.items():
		if valor>len(lista)/2:
			resu = chave
	return resu

assert dominante([0,0,0,1,2,0,3]) == 0
assert dominante([10,10,10]) == 10
assert dominante([1,2,2,3]) == -1 
