# Date: Tue, 27 Mar 2012 22:35:37 +0000
# Question 69
# JOAO PEDRO FERREIRA=20
# 21211940=20
dados1 = []=20
dados2 = []=20
for i in range(4):=20
	dados1.append(raw_input())=20
for i in range(4):=20
	dados2.append(raw_input())=20
if int(dados1[3]) > int(dados2[3]):=20
	print dados2[0]=20
elif int(dados2[3]) > int(dados1[3]):=20
	print dados1[0]=20
else:=20
	if int(dados1[2]) > int(dados2[2]):=20
		print dados2[0]=20
	elif int(dados2[2]) > int(dados1[2]):=20
		print dados1[0]=20
	else:=20
		if int(dados1[1]) > int(dados2[1]):=20
			print dados2[0]=20
		elif int(dados2[1]) > int(dados1[1]):=20
			print dados1[0]=20
		else:=20
			print "nenhuma"
