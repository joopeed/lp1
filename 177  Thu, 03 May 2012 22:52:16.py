# Date: Thu, 03 May 2012 22:52:16 +0000
# Question 177
# JOAO PEDRO FERREIRA DE MELO
# 21211940

medidas = {'km':1000,'hm':100,'dam':10,'m&#39=
;:1,'dm':0.1,'cm':0.01,'mm':0.001}

while True:
        valor1, uni1, valor2, uni2 = raw_input().split()
        valor1 = float(valor1)
        valor2 = float(valor2)
        if valor1==valor2==0: break
        resultado =  valor1*medidas[uni1] + valor2*medidas[uni2]
        print "%.2f m" % resultado
