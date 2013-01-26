# Date: Tue, 17 Apr 2012 23:27:25 +0000
# Question 136
# JOAO PEDRO FERREIRA
# 21211940
def eh_triangular_sup(mq):
        ok = 0
        for i in range(len(mq)):
                for j in range(len(mq[i])):
                        if i > j and mq[i][j]==0:
                                ok+=1
        tam = len(mq)
        print ok
        if ok == ((tam*tam/2)-(tam/2)):
                return True
        else:
                return False
