# coding: utf-8
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
if a <(c+b) and b<(a+c) and c<(b+a):
	if a==b==c:
		print "Equilátero"
	elif (a==b and a!=c)or(a==c and c!=a)or(b==c and a!=b):
		print "Isósceles"
	elif a!=b!=c:
		print "Escaleno"
else:	
	print "Não é triângulo"
