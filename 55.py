leia = map(int,raw_input().split())
maior = leia[0]
maior2 = leia[1]
for i in leia:
        if i > maior:
                maior2 = maior
                maior = i
        elif i > maior2:
                maior2 = i
print maior+maior2
