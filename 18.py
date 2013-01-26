# coding: utf-8
ano = int(raw_input())
if ano%400==0 or(ano%4==0 and not(ano%100==0)):
	print "%i é bissexto"%ano
else:
	print "%i não é bissexto"%ano
