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
