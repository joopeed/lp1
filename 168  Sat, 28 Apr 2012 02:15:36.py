# Date: Sat, 28 Apr 2012 02:15:36 +0000
# Question 168
# JOAO PEDRO LEONCIO 21211940
# PROGRAMACAO I - UFCG 2012.1 - JORGE ABRANTES
def ehsolucao(m):
        for i in range(len(m)):
                for j in range(len(m[0])):
                        for jj in range(len(m[0])):
                                if m[i][j] == m[i][jj] and j!=jj:
                                        return False
                        for ii in range(len(m)):
                                if m[i][j] == m[ii][j] and i!=ii:
                                        return False
        for i in range(3):
                for j in range(i*3,i*3+3):
                        for k in range(i*3,i*3+3):
                                for jj in range(i*3,i*3+3):
                                        for kk in range(i*3,i*3+3):
                                                if m[j][k]==m[jj][kk] a=
nd j!=jj and k!=kk:
                                                        return False
        return True

n = int(raw_input())
instancia =1
for i in range(n):
        matriz = []
        for j in range(9):
                matriz.append(map(int, raw_input().split()))
        print "Instancia", instancia
        if ehsolucao(matriz):
                print "SIM"
        else:
                print "NAO"
        instancia+=1
        print
        if i!=n-1:
                raw_input()
