# Date: Sun, 18 Mar 2012 01:48:39 +0000
# Question 38
# coding: utf-a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
if a <(c+b) and b<(a+c) and c<(b+a):
	if a==b==c:
		print "Equil=E1tero"
	elif (a==b and a!=c)or(a==c and c!=a)or(b==c and a!=b):
		print "Is=F3sceles"
	elif a!=b!=c:
		print "Escaleno"
else:=09
	print "N=E3o =E9 tri=E2ngulo"
