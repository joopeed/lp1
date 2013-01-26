def tem123plus(lista):
	ok = [-1,-1,-1]
	pos = -1
	resu = 0
	for i in range(len(lista)):
		if lista[i]==1 and ok[0]==-1:
			ok[0] =1
			pos = i
		if lista[i]==2 and ok[0]!=-1:
			ok[1] =1
		if lista[i]==3 and ok[1]!=-1:
			ok[2] =1
	for oks in ok:
		if oks>0:
			resu+=1
	if resu==3:
		return pos
	else:
		return -1
print tem123plus([3,2,1,2,3]), 2
print tem123plus([4,1,1,1,4,2,3]), 1
print tem123plus([1,2,2,3]), 0
print tem123plus([1,2,2,4]), -1

assert tem123plus([3,2,1,2,3]) == 2
assert tem123plus([4,1,1,1,4,2,3]) == 1
assert tem123plus([1,2,2,3]) == 0
assert tem123plus([1,2,2,4]) == -1


