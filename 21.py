valor = float(raw_input("Valor de venda? "))
simpost = valor/1.4	
print "ICMS:", simpost*0.18
print "IPI:", simpost*0.13
print "PIS:", simpost*0.014
print "Cofins:", simpost*0.076
print "Valor sem impostos:", simpost

