while True:
	x,y = map(int, raw_input().split())
	if x == (2 ** y):
		print x,y
		break
