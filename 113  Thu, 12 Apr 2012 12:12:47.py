# Date: Thu, 12 Apr 2012 12:12:47 +0000
# Question 113
# coding: utf-# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940
def conta_letra(letra, frase):
        conta=0
        for i in frase:
                if i.lower() == letra.lower():
                        conta+=1
        return conta
