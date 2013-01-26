# Date: Sun, 18 Mar 2012 01:41:22 +0000
# Question 18
# coding: utf-ano = int(raw_input())
if ano%400==0 or(ano%4==0 and not(ano%100==0)):
	print "%i =E9 bissexto"%ano
else:
	print "%i n=E3o =E9 bissexto"%ano
