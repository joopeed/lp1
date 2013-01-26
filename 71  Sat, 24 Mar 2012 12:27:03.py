# Date: Sat, 24 Mar 2012 12:27:03 +0000
# Question 71
# JOAO PEDRO FERREIRA=20
# 21211940
senha = raw_input()
somapar =0
somaimpar= 0
for i in range(len(senha)):
        if (i+1)%2!=0:
                somaimpar+= int(senha[i])
        else:
                somapar+=int(senha[i])
if somapar%2==0 and somaimpar%2!=0:
        print "segura"
else:
        print "insegura"
