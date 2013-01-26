for i in range(12):
	n,m = map(float,raw_input().split())
	lucro = n-m
	if lucro>=0:
		print " %.1f" % lucro
	else:
		print "%.1f" % lucro
