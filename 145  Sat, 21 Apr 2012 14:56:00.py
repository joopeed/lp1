# Date: Sat, 21 Apr 2012 14:56:00 +0000
# Question 145
# JOAO PEDRO LEONCIO - 21211940
## PROGRAMACAO I - JORGE ABRANTES - 2012.1
def acima_media(tab):
        medias = len(tab[0])*[0]
        for i in range(len(tab)):
                for j in range(len(tab[0])):
                        medias[j]+=tab[i][j]
        indices = []
        for i in range(len(medias)):
                if medias[i]/len(tab) >=7:
                        indices.append(i)
        return indices
