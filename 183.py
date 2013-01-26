soma = int(raw_input())
ints = map(int, raw_input().split())
resu = -1
for i in range(len(ints)):
	if i+ints[i]==soma and resu==-1:
		resu = i
print resu
