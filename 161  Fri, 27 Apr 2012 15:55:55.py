# Date: Fri, 27 Apr 2012 15:55:55 +0000
# Question 161
# JOAO PEDRO LEONCI# 21211940

def movimentos_diagonais(lab):=20
        conta=0=20
        for i in range(len(lab)):=20
                for j in range(len(lab[0])):=20
                        if lab[i][j]=='*':=20
                                if i+1 < len(lab) and j+1 < len(lab[0=
]):=20
                                        if lab[i+1][j+1]==" "=
:
                                                conta+=1=20
                                if i-1 >=0 and j-1 >=0:=20
                                        if lab[i-1][j-1]==" "=
:=20
                                                conta+=1=20
                                if i-1 >=0 and j+1 < len(lab[0]):=
=20
                                        if lab[i-1][j+1]==" "=
:=20
                                                conta+=1=20
                                if i+1 < len(lab) and j-1 >=0:=20
                                        if lab[i+1][j-1]==" "=
:=20
                                                conta+=1=20
        return conta
