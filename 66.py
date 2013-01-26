n = map(float, raw_input().split())
m =raw_input().split()
minimo = float(raw_input())
for i in range(len(n)):
        if n[i] <minimo:
                print m[i], n[i]


