# Date: Thu, 26 Apr 2012 12:23:01 +0000
# Question 157
# JOAO PEDRO LEONCI# 21211940
# PROGRAMACAO I - UFCG 2012.1
def eh_escalonada(m):
        for i in range(len(m)):
                for j in range(len(m)):
                        if i==j and m[i][j]!=1:
                                        return False
                        elif i!=j and m[i][j]!=0:
                                        return False
        return True
