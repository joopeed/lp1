# Date: Thu, 22 Mar 2012 12:07:28 +0000
# Question 55
# JOAO PEDRO FERREIRA
# 21211940
leia = map(int,raw_input().split())
maior = 0
maior2 = 0
for i in leia:
        if i > maior:
                maior2 = maior
                maior = i
        elif i > maior2 and maior2!=i:
                maior2 = i
print maior+maior2
