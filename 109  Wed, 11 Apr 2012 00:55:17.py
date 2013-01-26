# Date: Wed, 11 Apr 2012 00:55:17 +0000
# Question 109
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

cod =map(int, raw_input())
ok=0
for i in range(len(cod)-1):
        if not((cod[i]%2==0 and cod[i+1]%2!=0)or(cod[i]%2!=0 and co=
d[i+1]%2==0)):       ok=1
if ok!=1:
        print "verdadeiro:", len(cod),"algarismos."
else:
        print "falso:", len(cod),"algarismos."
