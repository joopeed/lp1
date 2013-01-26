# Date: Fri, 13 Apr 2012 14:40:18 +0000
# Question 100
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
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
