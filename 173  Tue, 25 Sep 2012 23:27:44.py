# Date: Tue, 25 Sep 2012 23:27:44 +0000
# Question 173
# JOAO PEDRO LEONCIO - 21211940=20
# UFCG 2012.1 - JORGE ABRANTES
def pagamento_IPVA(veiculos, mes):
        resu = []
        for i in range(len(veiculos)-1,-1,-1):
                if veiculos[i][-1] == str(mes):
                        resu.append(veiculos[i])
                        veiculos.pop(i)
        return resu[::-1]
