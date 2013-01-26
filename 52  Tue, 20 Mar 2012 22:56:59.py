# Date: Tue, 20 Mar 2012 22:56:59 +0000
# Question 52
# JOAO PEDRO FERREIRA
# 21211940
n = int(raw_input("n? "))
b =1
for i in range(1,3*(n/2),3):
        b = b * i
        print i
        print b
if n%2!=0:
        print i+3
