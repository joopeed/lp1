def filtra_altera_lista(num, lista):
	for i in range(len(lista)-1,-1,-1):
		if i%num!=0: 
			lista.pop(i)
			

lista1 = [0,1,2,3,4,5,6]
lista2 = [2,3,5,7,11,13,17]

filtra_altera_lista(2, lista1)
assert lista1 == [0,2,4,6]
filtra_altera_lista(3, lista1)
assert lista1 == [0,6]

filtra_altera_lista(3, lista2)
filtra_altera_lista(2, lista2)
assert lista2 == [2, 17]
