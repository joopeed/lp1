# Date: Wed, 25 Apr 2012 19:53:34 +0000
# Question 155
# JOAO PEDRO LEONCI# 21211940
def jogo_da_velha(jogo):
    for x in range(len(jogo)):
        for y in range(len(jogo[0])):
                if jogo[x][0]==jogo[x][1]==jogo[x][2] and jogo[x][1=
]!="-":
                        return "%s ganhou"%jogo[x][0]
                elif jogo[0][y]==jogo[1][y]==jogo[2][y] and jogo[1]=
[y]!="-":
                        return "%s ganhou"%jogo[0][y]
                elif jogo[0][0]==jogo[1][1]==jogo[2][2] and jogo[1]=
[1]!="-":
                        return "%s ganhou"%jogo[1][1]
                elif jogo[2][0]==jogo[1][1]==jogo[0][2] and jogo[1]=
[1]!="-":
                        return "%s ganhou"%jogo[1][1]

    return "Ninguem ganhou"
