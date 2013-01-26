# Date: Tue, 27 Mar 2012 22:46:02 +0000
# Question 80
# JOAO PEDRO FERREIRA
# 21211940
conta=0
while True:
 n =  raw_input()
 contavogais=0
 contacons=0
 conta+=1
 for i in n:
        if i.lower() in "aeiou":
                contavogais+=1
        else:
                contacons+=1
 if contacons > contavogais:
         break
print conta
