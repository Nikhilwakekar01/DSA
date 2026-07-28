nums = [1,1,1,2,2,3]


k=2
for i in range(2,len(nums)):
    if(nums[i]!=nums[k-2] ):
        print(i)
        print(nums)
        nums[k]=nums[i]
        k+=1
        print(nums)
   

print(nums)



