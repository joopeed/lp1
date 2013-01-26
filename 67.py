cpf = map(int,list(raw_input()))
s = 10
n = 11
soma =0
for i in range(9):
	soma+= cpf[i] *s
	s-= 1
dig1 = (10*soma) % 11
if dig1 == 10:
	dig1 =0
soma=0
for i in range(9):
	soma+= cpf[i] *n
	n-=1
soma+=dig1*n
dig2 = (10*soma) % 11
if dig2== 10:
	dig2 =0
resu = str(dig1) + str(dig2)
print resu
