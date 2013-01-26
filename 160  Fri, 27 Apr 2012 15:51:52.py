# Date: Fri, 27 Apr 2012 15:51:52 +0000
# Question 160
# JOAO PEDRO LEONCI# 21211940

def soma_linha(escalar,n1,n2,m):
        if n1 >=len(m) or n2 >= len(m) or n1 <0 or n2<0:
                return False
        for i in range(len(m[n1])):
                m[n2][i]+=m[n1][i]*escalar
        return True
