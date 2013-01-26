# Date: Wed, 26 Sep 2012 00:10:19 +0000
# Question 174
# JOAO PEDRO LEONCIO - 21211940=20
# UFCG 2012.1 - JORGE ABRANTES

def alcance_retweet(u, seguidores):
        resu = [0]*len(seguidores)
        for i in range(len(seguidores[u])):
                if seguidores[u][i] == 1:
                        resu[i] = 1
                        for j in range(len(seguidores[i])):
                                if seguidores[i][j] == 1:
                                        resu[j] = 1
        return resu
