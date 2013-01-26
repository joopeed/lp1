# Date: Thu, 12 Apr 2012 16:06:33 +0000
# Question 120
# JOAO PEDRO LEONCI# PROG 1 - ufcg 2012.1
# 21211940
def cria_login(nome):
        nome = nome.split()
        login = nome[0].lower()
        for i in range(1,len(nome)):
          if nome[i] not in "dodade":
                login+=nome[i][0].lower()
        return login
