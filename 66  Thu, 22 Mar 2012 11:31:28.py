# Date: Thu, 22 Mar 2012 11:31:28 +0000
# Question 66
# JOAO PEDRO FERREIRA
# 21211940
n = map(float, raw_input().split())
m =raw_input().split()
minimo = float(raw_input())
for i in range(len(n)):
        if n[i] <minimo:
                print m[i], n[i]

