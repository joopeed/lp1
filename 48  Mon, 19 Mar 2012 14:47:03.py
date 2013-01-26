# Date: Mon, 19 Mar 2012 14:47:03 +0000
# Question 48
# Joao Pedro Ferreira
# 21211940
a,b,k = map(int,raw_input().split())
for i in range(k+1):
        if i!=0 and i%a==0 and i%b==0:
                print i
