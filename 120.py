# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def cria_login(nome):
        nome = nome.split()
        login = nome[0].lower()
        for i in range(1,len(nome)):
          if nome[i] not in "dodade":
                login+=nome[i][0].lower()
        return login
print cria_login("Matheus Gaudencio do Rego")
assert cria_login("Eliane Araujo") == "elianea"

assert cria_login("Dalton Serey Guerrero") == "daltonsg"
