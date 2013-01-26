# Date: Wed, 26 Sep 2012 22:36:32 +0000
# Question 183
#JOAO PEDRO LEONCIO -  21211940
# 2012.1 - JORGE ABRANTES

soma = int(raw_input())
ints = map(int, raw_input().split())
resu = -1
for i in range(len(ints)):
        if i+ints[i]==soma and resu==-1:
                resu = i
print resu
