# Date: Wed, 25 Apr 2012 19:52:10 +0000
# Question 154
# JOAO PEDRO LEONCI# 21211940
def professores(alocacao, disc):
        conta=0
        for chave in alocacao.keys():
                if chave==disc:
                        for i in alocacao[chave]:
                                conta+=1
        return conta
