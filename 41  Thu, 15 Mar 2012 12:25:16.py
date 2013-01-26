# Date: Thu, 15 Mar 2012 12:25:16 +0000
# Question 41
lista=[for i in range(3):
	lista.append(raw_input())
maior = lista[0]
if(len(lista[0])<len(lista[1])):
	maior = lista[1]
	if(len(lista[1])<len(lista[2])):
		maior = lista[2]
elif(len(lista[0])<len(lista[2])):
	maior =lista[2]
	if(len(lista[2])<len(lista[1])):
		maior=lista[1]
print maior
