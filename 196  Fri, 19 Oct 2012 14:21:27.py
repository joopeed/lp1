# Date: Fri, 19 Oct 2012 14:21:27 +0000
# Question 196
def complemento_de_dois(numero):
=09
	num = bin(numero)[2:]
	if numero <0:
		num = num[1:]
	num = (8-len(num))*'0'+num
	if numero < 0:
		inverte = False
		c2= ""
		mag = ""
		for i in range(len(num)-1,-1,-1):
			if num[i] == "1":
				if inverte:
					mag+="0"
				else:=09
					mag+="1"
				inverte = True
			else:
				if inverte:
					mag+="1"
				else:
					mag+="0"
		c2+=mag[::-1]
	else:
		c2 = num
	return c2
