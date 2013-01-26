# Date: Fri, 04 May 2012 23:54:22 +0000
# Question 170
#coding: utf-# Jo=E3o Pedro Le=F4ncio
# 21211940
# Programa=E7=E3o 1 - UFCG 2012.1
# Prof. Jorge Abrantes

def move_inimigo(labirinto):

	limitex = len(labirinto)
	limitey = len(labirinto[0])

        for i in range(limitex):
                for j in range(limitey):

                        if labirinto[i][j] =='*':
                                alvo = (i,j)

                        if labirinto[i][j] =='X':
                                inimigo = (i,j)

	x1,y1 = alvo
	x2,y2 = inimigo
        horizontal = y1 - y2
        vertical = x1 - x2
=09
=09
	if horizontal ==0:
		if vertical >0:
			#i+1
	 	  	if x2+1 < limitex:
                        	if labirinto[x2+1][y2]=='*':
                                        	labirinto[x2+1][y2] = 'X&#39=
;
						labirinto[x2][y2] = ' '
                                        	return True
                                elif labirinto[x2+1][y2]==' ':
                                        	labirinto[x2+1][y2] = 'X&#39=
;
						labirinto[x2][y2] = ' '
                                        	return False
		elif vertical <0:
			#i-1
			if x2-1 >=0:
                             	if labirinto[x2-1][y2]=='*':
                               		labirinto[x2-1][y2] = 'X'
					labirinto[x2][y2] = ' '
                                	return True
                                elif labirinto[x2-1][y2]==' ':
                                        labirinto[x2-1][y2] = 'X'
					labirinto[x2][y2] = ' '
                                        return False
	elif vertical ==0:
		if horizontal >0:
			# j+1
			if y2+1 < limitey:
				if labirinto[x2][y2+1]=='*':
					labirinto[x2][y2+1] = 'X'
					labirinto[x2][y2] = ' '
					return True
				elif labirinto[x2][y2+1]==' ':
					labirinto[x2][y2+1] = 'X'
					labirinto[x2][y2] = ' '
					return False
		elif horizontal <0:
			# j-1=09
			if y2-1 >=0:
			        if labirinto[x2][y2-1]=='*':
			                labirinto[x2][y2-1] = 'X'
					labirinto[x2][y2] = ' '
			                return True
			        elif labirinto[x2][y2-1]==' ':
			                labirinto[x2][y2-1] = 'X'
					labirinto[x2][y2] = ' '
			                return False
	else:
		if horizontal >0:
			# j+1
			if y2+1 < limitey:
				if labirinto[x2][y2+1]=='*':
					labirinto[x2][y2+1] = 'X'
					labirinto[x2][y2] = ' '
					return True
				elif labirinto[x2][y2+1]==' ':
					labirinto[x2][y2+1] = 'X'
					labirinto[x2][y2] = ' '
					return False
		elif horizontal <0:
			# j-1=09
			if y2-1 >=0:
			        if labirinto[x2][y2-1]=='*':
			                labirinto[x2][y2-1] = 'X'
					labirinto[x2][y2] = ' '
			                return True
			        elif labirinto[x2][y2-1]==' ':
			                labirinto[x2][y2-1] = 'X'
					labirinto[x2][y2] = ' '
			                return False
		if vertical >0:
			#i+1
	 	  	if x2+1 < limitex:
                        	if labirinto[x2+1][y2]=='*':
                                        	labirinto[x2+1][y2] = 'X&#39=
;
						labirinto[x2][y2] = ' '
                                        	return True
                                elif labirinto[x2+1][y2]==' ':
                                        	labirinto[x2+1][y2] = 'X&#39=
;
						labirinto[x2][y2] = ' '
                                        	return False
		elif vertical <0:
			#i-1
			if x2-1 >=0:
                             	if labirinto[x2-1][y2]=='*':
                               		labirinto[x2-1][y2] = 'X'
					labirinto[x2][y2] = ' '
                                	return True
                                elif labirinto[x2-1][y2]==' ':
                                        labirinto[x2-1][y2] = 'X'
					labirinto[x2][y2] = ' '
                                        return False
