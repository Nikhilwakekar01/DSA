nums= [30 ,8,23, 6, 10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26]
target=86

nums.sort()
result_sum=0
print(nums)
for i in range(len(nums)-2):
    left=i+1
    right=len(nums)-1
    
    

    while(left<right):
        sum= nums[i]+nums[left]+nums[right]
        if(sum<target):
            result_sum=result_sum+(right-left)
            left+=1
            
        elif(sum>=target):
            right-=1

print(result_sum)
        
       




print(result_sum)
  

