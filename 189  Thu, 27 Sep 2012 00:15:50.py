# Date: Thu, 27 Sep 2012 00:15:50 +0000
# Question 189
p1 = raw_input(p2 = raw_input()
dic = {}
resu = ""
for l in p2:
        if l.lower() not in p1.lower():
                resu+=l
print resu
