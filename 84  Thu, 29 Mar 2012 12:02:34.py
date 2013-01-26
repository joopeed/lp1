# Date: Thu, 29 Mar 2012 12:02:34 +0000
# Question 84
# JOAO PEDRO FERREIRA
# 21211940
ok =0
for i in raw_input():
        if i.lower() in "aeiou":
                ok = 1
                break
if ok ==0:
        print "-"
else:
        print  i
