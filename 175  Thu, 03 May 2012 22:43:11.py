# Date: Thu, 03 May 2012 22:43:11 +0000
# Question 175
# JOAO PEDRO FERREIRA DE MELO
# 21211940

def senha(cadastro, user):
        for chave,valor in cadastro.items():
                if user in valor:
                        return chave
        return -1
