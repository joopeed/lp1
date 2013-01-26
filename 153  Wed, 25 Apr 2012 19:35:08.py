# Date: Wed, 25 Apr 2012 19:35:08 +0000
# Question 153
# JOAO PEDRO LEONCI# 21211940

def turma_pratica(alocacao,t):
        conta=0
        for chave, valor in alocacao.items():
                if valor == t:
                        conta+=1
        return conta
