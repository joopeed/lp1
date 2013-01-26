# Date: Wed, 26 Sep 2012 00:29:45 +0000
# Question 180
# JOAO PEDRO LEONCIO - 21211940=20
# UFCG 2012.1 - JORGE ABRANTES
def colegas_de_sala(salasprofs, professor):
        resu = []
        for prof, sala in salasprofs.items():
                if salasprofs[professor] == sala and professor!=prof:
                        resu.append(prof)
        return resu
