# Date: Wed, 26 Sep 2012 23:49:11 +0000
# Question 182
p1 = raw_input(p2 = raw_input()
dic = {}
resu = ""
for l in p1:
        if l not in dic:
                dic[l]=1
for l in p2:
        if l not in dic:
                resu+=l
print resu
