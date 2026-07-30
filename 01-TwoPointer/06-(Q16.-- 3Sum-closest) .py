nums = [-1,2,1,-4]
target = 1

nums.sort()
result=[]
print(nums)
for i in range(len(nums)-2):
    
    
    if(i>0 and nums[i]==nums[i-1]):
        
        continue
    left=i+1
    right=len(nums)-1
    sum= -1*nums[i]
    max_diff=float('inf')

    while(left<right):
        
        
        print("hello")
        if(nums[left]+nums[right]==sum):
            diff=abs(sum-target)
            if(diff<max_diff):
                max_diff=diff
            
            result=sum
            left+=1
            right-=1
        elif(nums[left]+nums[right]<sum):
           
            left+=1
        elif(nums[left]+nums[right]>sum):
            
            right-=1





print(result)
  

