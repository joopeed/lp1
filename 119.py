# coding: utf-8
# Programacao 1 - 2012.1 - Jorge Abrantes
# João Pedro Leôncio	
# 21211940

def eh_vencedor_linea(tabuleiro):
	ok= False
	atual =0
	while True: 
		atual = tabuleiro[atual]
		if atual>len(tabuleiro)-1 or atual<0:
                        break
		if atual==0:
			ok=True
			break
	return ok

assert eh_vencedor_linea([2,0,1])
print eh_vencedor_linea([8,0,1])
assert not eh_vencedor_linea([1,2,3])

assert eh_vencedor_linea([1,2,3,4,5,0])
assert not eh_vencedor_linea([5,0,0,0,0,8])
