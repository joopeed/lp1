# Date: Fri, 19 Oct 2012 14:00:13 +0000
# Question 199
# JOAO PEDRO FERREIRA DE MELO LEONCIO
# PROG1 UFCG 2012.1

def ajeita_pedido(lista):
        acom = 0
        mass = 0
        molh = 0
        for ele in lista:
                if ele in range(0,8):
                        mass +=1
                elif ele in range(100,104):
                        molh +=1
                elif ele in range(1000,1016):
                        acom +=1
                else:
                        return []
        if molh==2 and acom==4 and mass==1:
                return sorted(lista)
        else:
                return []
