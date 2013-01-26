import math
valor = float(raw_input("Valor? "))
print "Sem arredondamento:", valor**2
print "Com arredondamento para cima:", math.ceil(valor**2)
print "Com arredondamento para baixo:", math.floor(valor**2)
print "Valor truncado:", int(valor**2)
