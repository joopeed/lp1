p1 = raw_input()
p2 = raw_input()
resu = ""
for l in p2:
	if l.lower() not in p1.lower():
		resu+=l

print resu

