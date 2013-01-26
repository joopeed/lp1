# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

senha = raw_input()
ok=True


for i in range(len(senha)):
	if i%2!=0:
		if int(senha[i])%2!=0:
			ok = False
	else:
		if int(senha[i])%2==0:
			ok = False

if ok:
	print "segura"
else:
	print "insegura"
