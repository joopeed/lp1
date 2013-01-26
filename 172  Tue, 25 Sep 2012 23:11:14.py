# Date: Tue, 25 Sep 2012 23:11:14 +0000
# Question 172
# JOAO PEDRO LEONCIO - 21211940
# UFCG 2012.1 - JORGE ABRANTES

def inverte3a3(palavra):
        resu = ""
        for i in range(len(palavra)/3,-1,-1):
                resu+=palavra[i*3:i*3+3]
        return resu
