# Date: Tue, 27 Mar 2012 22:48:16 +0000
# Question 82
# JOAO PEDRO FERREIRA
# 21211940
n = int(raw_input())
while True:
        print n
        if n==1: break
        if n%2==0:
                n/=2
        else:
                n = 3*n+1
