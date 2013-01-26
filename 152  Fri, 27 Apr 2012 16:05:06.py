# Date: Fri, 27 Apr 2012 16:05:06 +0000
# Question 152
def desempenho(m)        conta=0
        for i in range(len(m)):
                for j in range(len(m[0])):
                        if m[i][j] == 1:
                                conta+=1
        return conta
