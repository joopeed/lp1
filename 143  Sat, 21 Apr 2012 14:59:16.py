# Date: Sat, 21 Apr 2012 14:59:16 +0000
# Question 143
# JOAO PEDRO LEONCIO - 21211940
## PROGRAMACAO I - JORGE ABRANTES - 2012.1
from graphics import *

def clicou_no_retangulo(p1,p2,ck):
        x1 = p1.getX()
        y1 = p1.getY()
        x2 = p2.getX()
        y2 = p2.getY()
        cx = ck.getX()
        cy = ck.getY()
        if x2 >= x1 and y2 >= y1 and cx <= x2 and cx >==
 x1 and cy >= y1 and cy <= y2:
                return True
        elif x2 >= x1 and y2 <= y1 and cx <= x2 and cx >=
= x1 and cy <= y1 and cy >= y2:
                return True
        elif x2 <= x1 and y2 >= y1 and cx >= x2 and cx <=
= x1 and cy >= y1 and cy <= y2:
                return True
        elif x2 <= x1 and y2 <= y1 and cx >= x2 and cx <=
= x1 and cy <= y1 and cy >= y2:
                return True
        else:
                return False
