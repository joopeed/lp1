# Date: Sun, 18 Mar 2012 01:41:56 +0000
# Question 19
i = int(raw_input("Km inicial? "))
f = int(raw_input("Km final? "))
r = f-i
l = int(raw_input("Litros? "))
v = float(raw_input("Total recebido? "))
print "Consumo em Km/L:", r/l
print "Lucro liquido:",v-(l*2.55)
