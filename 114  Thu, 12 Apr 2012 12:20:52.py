# Date: Thu, 12 Apr 2012 12:20:52 +0000
# Question 114
# coding: utf-# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940

def encontra_menores(num, lista):
        valor =-1
        for i in lista:
                if i < num:
                        valor =i
                        break
        return valor
