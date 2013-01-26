# Date: Mon, 02 Apr 2012 14:41:39 +0000
# Question 96
# JOAO PEDRO LEONCI# 21211940
def tem_vogais_adjacentes(palavra):
        p = palavra[0]
        ok =0
        for i in palavra:
                if p.lower() in "aeiou" and i.lower() in "ae=
iou":
                        ok = 1
                p = i
        if ok ==1:
                return "sim"
        else:
                return "nao"

assert tem_vogais_adjacentes("orfeu") == "sim"

assert tem_vogais_adjacentes("brasil") == "nao"

assert tem_vogais_adjacentes("voo") == "sim"

n = raw_input()
print tem_vogais_adjacentes(n)
