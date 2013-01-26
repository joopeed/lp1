# Date: Thu, 26 Apr 2012 12:41:02 +0000
# Question 158
# JOAO PEDRO LEONCI# 21211940
# PROGRAMACAO I - UFCG 2012.1

def troca_linhas(lin1, lin2, m):
        try:
                m[lin2],m[lin1] = m[lin1], m[lin2]
                return True
        except:
                return False
