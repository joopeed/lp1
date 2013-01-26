n = int(raw_input("n? "))
c = raw_input("c? ")
while (n):
        p = raw_input("palavra? ")
        if p[0].lower() == c.lower():
                print p, "comeca com", c
        else:
                print p, "nao comeca com", c
        n-=1
