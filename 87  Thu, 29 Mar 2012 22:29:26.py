# Date: Thu, 29 Mar 2012 22:29:26 +0000
# Question 87
# coding: utf-# JOAO PEDRO FERREIRA DE MELO
# 21211940
p1 = map(int, raw_input().split())
p2 = raw_input().split()
while True:
        conta =0
        indice =0
        n, k = map(int, raw_input().split())
        if n==0 and k==0: break
        for i in range(len(p1)):
             if p1[i] <= k:
                conta+=1
                indice=i
             if conta == n:
                break
        if not(conta!=n):
                print p2[i], p1[i]
        else:
                print "-"
