n = raw_input()
palavra = ""
for i in range(len(n)):
	if i%2==0:
		palavra += n[i]	
print palavra
