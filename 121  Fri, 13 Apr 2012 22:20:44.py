# Date: Fri, 13 Apr 2012 22:20:44 +0000
# Question 121
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def conta_dias(dia, mes, ano):
        soma = 0
        for i in range(1,mes+1):
                if mes!=i:
                        if i in [1,3,5,7,8,10,12]:
                                soma+=31
                        elif i ==2:
                                if ano%400==0 or(ano%4==0 and not(a=
no%100==0)):
                                        soma+=29
                                else:
                                        soma+=28
                        else:
                                soma+=30
        soma+=dia
        return soma
