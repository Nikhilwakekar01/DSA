nums=[2,0,2,1,1,0]
n=len(nums)
noofone=0
noofzero=0
for i in range(n):
    if(nums[i]==0):
        noofzero+=1
    elif(nums[i]==1):
        noofone+=1
for i in range(n):
    if(i<noofzero):
        nums[i]=0
    elif(i<noofzero+noofone):
        nums[i]=1
    else:
        nums[i]=2
        
print(nums)




  

