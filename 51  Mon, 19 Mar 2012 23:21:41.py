# Date: Mon, 19 Mar 2012 23:21:41 +0000
# Question 51
# JOAO PEDRO FERREIRA
# 21211940
p = raw_input()
a=0
e=0
ii=0
o=0
u=0
for i in p:
        if i.lower() == 'a':
                a+=1
        elif i.lower() == 'e':
                e+=1
        elif i.lower() == 'i':
                ii+=1
        elif i.lower() == 'o':
                o+=1
        elif i.lower() == 'u':
                u+=1
print "A -",a
print "E -",e
print "I -",ii
print "O -",o
print "U -",u
