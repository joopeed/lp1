# Date: Fri, 13 Apr 2012 14:55:46 +0000
# Question 127
# coding: utf-# Programacao 1 - 2012.1 - Jorge Abrantes
# Jo=E3o Pedro Le=F4ncio   =20
# 21211940

def indices_de_idosos(fila):
        idosos = []
        for i in range(len(fila)):
                if fila[i] > 60:
                        idosos.append(i)
        return idosos
