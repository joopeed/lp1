# coding: utf-8
while True:
        n = int(raw_input("Número 1: "))
        if n >=0 and n<=100:
                break
        print "Número 1 inválido. Por favor, digite novamente."
while True:
        b = int(raw_input("Número 2: "))
        if b>=0 and b<=100:
                break
        print "Número 2 inválido. Por favor, digite novamente."
print "Soma:", n+b
