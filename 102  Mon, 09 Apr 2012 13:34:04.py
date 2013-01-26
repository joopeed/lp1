# Date: Mon, 09 Apr 2012 13:34:04 +0000
# Question 102
# coding: utf-# JOAO PEDRO FERREIRA DE MELO LEONCIO
# PROG1 - UFCG 2012.1
# 21211940
nums = map(int, raw_input().split())
nomes = raw_input().split()

soma =0

for i in nums:
        soma+=i

media = soma/len(nums)

for i in range(len(nums)):
        if nums[i] > media:
                print nomes[i], nums[i]

