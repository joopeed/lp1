def tem123(lista):
	resu = -1
	for i in range(len(lista)-2):
		if lista[i]==1 and lista[i+1]==2 and lista[i+2]==3:
			resu = i
	return resu

assert tem123([1,2,3]) == 0
assert tem123([1,1,1,1,2,3]) == 3
assert tem123([1,2,2,3]) == -1


