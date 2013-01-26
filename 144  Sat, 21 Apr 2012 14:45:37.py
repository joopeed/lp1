# Date: Sat, 21 Apr 2012 14:45:37 +0000
# Question 144
# JOAO PEDRO LEONCIO - 21211940
## PROGRAMACAO I - JORGE ABRANTES - 2012.1
def calcula_media(tab):
        medias = []
        for i in range(len(tab)):
                aluno = 0
                for j in range(len(tab[0])):
                        aluno+=tab[i][j]
                medias.append("%.1f" %(aluno/len(tab[0])))
        return medias
