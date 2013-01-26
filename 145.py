def acima_media(tab):
    medias = []
    for j in range(len(tab[0])):
	media = 0 # Tu esqueceu de zerar a media
        cont = 0
        soma = 0
        for i in range(len(tab)):
            soma += tab[i][j]
            cont += 1
        media = soma/cont # E a media a uma pra cada coluna por isso ela fica mais atras
        if media >= 7.0: # Do mesmo jeito isso aqui tem que fazer esse teste toda vez, a cada coluna.
		##### OBSERVE QUE NAO PRECISA MAIS DO AND j not in medias =p
            medias.append(j) # Do outro jeito, tava fazendo isso pra cada linha e pra cada coluna, sa bastava a media chegar a 7, ja appendava! =p
    return medias
# Vejamos se assim funciona
tab = [
 [ 7.0, 2.0,  5.0,  8.0,  6.0],
 [ 8.0, 1.0,  5.0,  8.0,  6.0],
 [ 9.0, 0.0,  8.0, 10.0,  4.0],
 [10.0, 1.0, 10.0,  6.0,  7.0],
]
print acima_media(tab)
