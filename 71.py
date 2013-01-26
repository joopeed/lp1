# JOAO PEDRO FERREIRA 
# 21211940 
senha = raw_input() 
somapar =0 
somaimpar= 0 
for i in range(len(senha)): 
	if (i+1)%2!=0: 
		somaimpar+= int(senha[i]) 
	else: 
		somapar+=int(senha[i]) 
if somapar%2==0 and somaimpar%2!=0: 
	print "segura" 
else: 
	print "insegura"

