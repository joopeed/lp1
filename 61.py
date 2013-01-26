x = float(raw_input())
y = float(raw_input())
if x==y==0:
	print "Origem"
elif x==0 and y!=0:
	print "Eixo das ordenadas"
elif y==0 and x!=0:
	print "Eixo das abscissas"
elif x >0 and y>0:
	print "Primeiro quadrante"
elif x<0 and y>0:
	print "Segundo quadrante"
elif x<0 and y<0:
	print "Terceiro quadrante"
else:
	print "Quarto quadrante"
