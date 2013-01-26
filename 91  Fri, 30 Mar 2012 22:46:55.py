# Date: Fri, 30 Mar 2012 22:46:55 +0000
# Question 91
# JOAO PEDRO LEONCI# 21211940
conta=0
nums = map(int, raw_input().split())
for i in range(len(nums)):
        for j in range(i,len(nums)):
                if nums[j] == nums[i]:
                        conta+=1
if conta >3:
        print conta/2
else:
        print 0
