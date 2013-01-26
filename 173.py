def pagamento_IPVA(veiculos, mes):
	resu = []
	for i in range(len(veiculos)-1,-1,-1):
		if veiculos[i][-1] == str(mes):
			resu.append(veiculos[i])
			veiculos.pop(i)
	return resu[::-1]

veiculos = ['NYX1232', 'MNS8735', 'MNP8822', 'MFG9820', 'NPS1871'] 
print pagamento_IPVA(veiculos,1) == ['NPS1871'] 
print veiculos == ['NYX1232', 'MNS8735', 'MNP8822', 'MFG9820'] 
assert pagamento_IPVA(veiculos,2) == ['NYX1232', 'MNP8822'] 
assert veiculos == ['MNS8735', 'MFG9820'] 
