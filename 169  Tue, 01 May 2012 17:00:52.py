# Date: Tue, 01 May 2012 17:00:52 +0000
# Question 169
# Joao Pedro Ferreira de Melo
# 21211940=20
def lab2str(lab):
	str = [(len(lab[0])+2)*["="] for i in range(len(lab)+2)]
	for i in range(1,len(str)-1):
		str[i][0]=str[i][len(str[0])-1]='|'
		for j in range(1,len(str[0])-1):
			if lab[i-1][j-1] != 'P':
				str[i][j] = lab[i-1][j-1]
			else:
				str[i][j] = '#'
	result = ""
	for i in range(len(str)-1):
		result += "".join(str[i])+"\n"
	result += "".join(str[len(str)-1])
	return result
