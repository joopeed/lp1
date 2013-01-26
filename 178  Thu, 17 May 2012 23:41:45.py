# Date: Thu, 17 May 2012 23:41:45 +0000
# Question 178
def juncao_ordenada(l1,l2):
        i = 0
        j = 0
        l3 =[]
        while i< len(l1) and j <len(l2):
                if l1[i] <= l2[j]:
                        l3.append(l1[i])
                        i+=1
                else:
                        l3.append(l2[j])
                        j+=1
        if i==len(l1):
                l3 = l3 + l2[j:]
        elif j==len(l2):
                l3 = l3 + l1[i:]
        return l3
