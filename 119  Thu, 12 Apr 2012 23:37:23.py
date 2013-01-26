# Date: Thu, 12 Apr 2012 23:37:23 +0000
# Question 119
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def eh_vencedor_linea(tabuleiro):
        ok= False
        atual =0
        while True:
                atual = tabuleiro[atual]
                if atual>len(tabuleiro)-1 or atual<0:
                        break
                if atual==0:
                        ok=True
                        break
        return ok
