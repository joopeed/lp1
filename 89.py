menor = 1000000000000000000000000000000000
maior = 0
while True:
	num = int(raw_input())
	if num ==-1: break
	if num > maior:
		maior =num
	if num < menor:
		menor =num
print "maior:" ,maior
print "menor:", menor
