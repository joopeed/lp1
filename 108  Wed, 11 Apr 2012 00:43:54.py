# Date: Wed, 11 Apr 2012 00:43:54 +0000
# Question 108
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def prevogais(palavra):
        lista =[]
        for i in range(len(palavra)-1):
                if palavra[i+1] in "AEIOUaeiou":
                        lista.append(palavra[i])
        return lista

assert prevogais("exemplo") == ['x', 'l']

assert prevogais("hiato") == ['h', 'i', '=
t']

