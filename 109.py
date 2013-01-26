# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

cod =map(int, raw_input())
ok=0
for i in range(len(cod)-1):
	if not((cod[i]%2==0 and cod[i+1]%2!=0)or(cod[i]%2!=0 and cod[i+1]%2==0)):	ok=1
if ok!=1:
	print "verdadeiro:", len(cod),"algarismos."
else:
	print "falso:", len(cod),"algarismos."

