# Date: Tue, 20 Mar 2012 00:17:56 +0000
# Question 53
# JOAO PEDRO FERREIRA
# 21211940
n = int(raw_input("n? "))
c = raw_input("c? ")
while (n):
        p = raw_input("palavra? ")
        if p[0].lower() == c.lower():
                print p, "comeca com", c
        else:
                print p, "nao comeca com", c
        n-=1
