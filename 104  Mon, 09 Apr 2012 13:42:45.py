# Date: Mon, 09 Apr 2012 13:42:45 +0000
# Question 104
# coding: utf-# JOAO PEDRO FERREIRA DE MELO LEONCIO
# PROG1 - UFCG 2012.1
# 21211940
def acima_de(N,L):
        lista = []
        for i in range(len(L)):
                if L[i] >N:
                        lista.append(i)
        return lista

nums = map(int, raw_input().split())
nomes = raw_input().split()

soma =0

for i in nums:
        soma+=i

media = soma/len(nums)

for i in acima_de(media,nums):
        print nomes[i], nums[i]

