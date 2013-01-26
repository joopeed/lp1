# Date: Wed, 26 Sep 2012 00:17:50 +0000
# Question 179
# JOAO PEDRO LEONCIO - 21211940=20
# UFCG 2012.1 - JORGE ABRANTES

def indices_de_idosos(fila):
        resu =[]
        for i in range(len(fila)):
                if fila[i] >60:
                        resu.append(i)
        return resu
