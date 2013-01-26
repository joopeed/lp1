# Date: Wed, 21 Mar 2012 23:48:13 +0000
# Question 60
# coding: utf-n = raw_input().split()
conta = 0
for i in n:
	if i=="Grave":
		conta+=5
	elif i=="Grav=EDssima":
		conta+=7
	elif i=="M=E9dia":
		conta+=4
	elif i=="Leve":
		conta+=3
if conta >=20:
	print conta,"pontos. CNH suspensa."
else:
	print conta,"pontos. CNH v=E1lida."
