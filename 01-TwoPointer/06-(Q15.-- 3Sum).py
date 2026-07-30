nums = [-1,0,1,2,-1,-4]

nums.sort()
result=[]
print(nums)
for i in range(len(nums)-2):
    
    
    if(i>0 and nums[i]==nums[i-1]):
        
        continue
    left=i+1
    right=len(nums)-1
    sum= -1*nums[i]

    while(left<right):
        print("hello")
        if(nums[left]+nums[right]==sum):
            
            result.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1
            while(left<len(nums) and nums[left]==nums[left-1]):
                
                left+=1
            while(right>=0 and nums[right]==nums[right+1]):
                
                right-=1
        elif(nums[left]+nums[right]<sum):
           
            left+=1
        elif(nums[left]+nums[right]>sum):
            
            right-=1





print(result)
  

