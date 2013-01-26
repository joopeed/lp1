# Date: Fri, 27 Apr 2012 16:00:25 +0000
# Question 151
def procura_elemento(m,ele):
        result = (-1,-1)
        for i in range(len(m)):
                for j in range(len(m[0])):
                        if m[i][j] == ele:
                                result = (i,j)
        return result
