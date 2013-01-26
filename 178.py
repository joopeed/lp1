def juncao_ordenada(l1,l2):
	i = 0
	j = 0
	l3 =[]
	while i< len(l1) and j <len(l2):
		if l1[i] <= l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i==len(l1):
		l3 = l3 + l2[j:]
	elif j==len(l2):
		l3 = l3 + l1[i:]
	return l3

lista1=[8,12,14,78,79,100,511]
lista2=[6,7,8,90,121,302]

assert juncao_ordenada(lista1,lista2) == [6, 7, 8, 8, 12, 14, 78, 79, 90, 100, 121, 302, 511]

print juncao_ordenada([1,2],[1])
