# Date: Thu, 29 Mar 2012 12:03:28 +0000
# Question 83
# JOAO PEDRO FERREIRA
# 21211940
while True:
        n = raw_input()
        if n =="fim": break
        ok=0
        for i in n:
                if i.upper() in "AEIOU":
                        print i
                        ok = 1
                        break
        if ok ==0:
                print "-"

