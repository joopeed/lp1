# Date: Sat, 21 Apr 2012 14:34:29 +0000
# Question 140
# JOAO PEDRO LEONCIO - 21211940
## PROGRAMACAO I - JORGE ABRANTES - 2012.1
def move_direita(lab):
        for i in range(len(lab)):
                for j in range(len(lab[0])):
                        if lab[i][j] == '*':
                                if j+1 < len(lab[0]):
                                        if lab[i][j+1]==" ":
                                                lab[i][j] = " "
                                                lab[i][j+1] = '*'
                                                return (i,j+1)
                                        else:
                                                return (i,j)
                                else:
                                        return (i,j)
