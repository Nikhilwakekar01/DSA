nums = [0,0,0]
target = 1

nums.sort()
result_sum=0
print(nums)
for i in range(len(nums)-2):
    
    
    if(i>0 and nums[i]==nums[i-1]):
        
        continue
    left=i+1
    right=len(nums)-1
    sum= nums[i]+nums[left]+nums[right]
    max_diff=float('inf')

    diff=abs(sum-target)
    if(diff<max_diff):
        max_diff=diff
        result_sum=sum

    while(left<right):
        
        
        print("hello")
        if(target==sum):
            diff=abs(sum-target)
            if(diff<max_diff):
                max_diff=diff
            
            result=sum
            left+=1
            right-=1
        elif(sum<target):
            left+=1
        elif(sum>target):
            right-=1





print(result_sum)
  

