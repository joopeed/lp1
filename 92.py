nomes = raw_input().split()
idades = map(int, raw_input().split())
for i in range(len(idades)):
	if idades[i] >=18:
		print nomes[i]
