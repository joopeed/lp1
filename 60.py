# coding: utf-8
n = raw_input().split()
conta = 0
for i in n:
	if i=="Grave":
		conta+=5
	elif i=="Gravíssima":
		conta+=7
	elif i=="Média":
		conta+=4
	elif i=="Leve":
		conta+=3
if conta >=20:
	print conta,"pontos. CNH suspensa."
else:
	print conta,"pontos. CNH válida."
