# Date: Sat, 24 Mar 2012 12:03:14 +0000
# Question 69
# JOAO PEDRO FERREIRA
# 21211940
dados1 = []
dados2 = []
for i in range(4):
        dados1.append(raw_input())
for i in range(4):
        dados2.append(raw_input())
if int(dados1[3]) > int(dados2[3]):
        print dados2[0]
elif int(dados2[3]) > int(dados1[3]):
        print dados1[0]
else:
        if int(dados1[2]) > int(dados2[2]):
                print dados2[0]
        elif int(dados2[2]) > int(dados1[2]):
                print dados1[0]
        else:
                if int(dados1[1]) > int(dados2[1]):
                           print dados2[0]
                elif int(dados2[1]) > int(dados1[1]):
                           print dados1[0]
                else:
                        print "nenhuma"
