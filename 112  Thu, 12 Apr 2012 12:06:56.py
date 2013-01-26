# Date: Thu, 12 Apr 2012 12:06:56 +0000
# Question 112
# coding: utf-# PROG 1 - UFCG 2012.1
# JOAO PEDRO FERREIRA
# 21211940

num = int(raw_input())
soma = 0
for i in range(1,num):
                if num%i==0:
                        soma+=i
if soma == num:
        print num, "=E9 um n=FAmero perfeito."
else:
        print num, "n=E3o =E9 um n=FAmero perfeito."
