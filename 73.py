n = raw_input()
soma = 0
while n!="***":
	if not(n[0] in "AEIOUaeiou"):
		soma+=1
	n = raw_input()
print "Palavras:", soma  
