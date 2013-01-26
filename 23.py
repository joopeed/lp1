import math
c = float(raw_input("Comprimento? "))
l = float(raw_input("Largura? "))
a = float(raw_input("Altura? "))
area = 2*c*a+2*l*a
print "Quantidade de caixas:",int(math.ceil(area/1.5))

