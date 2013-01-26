p = raw_input()
for i in p:
	if i in "aeiouAEIOU":
		print "<%c> sim"%i
	else:
		print "<%c> nao"%i
