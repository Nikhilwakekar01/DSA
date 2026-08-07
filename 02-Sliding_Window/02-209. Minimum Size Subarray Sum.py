
def minSize(nums,target):

    low=0
    high=0
    res=float('inf')
    sum=0

    while(high<len(nums)):
        sum=sum+nums[high]
        while(sum>=target):
            length=high-low+1
            res=min(res,length)
            sum=sum-nums[low]
            low+=1
        high+=1
    
    if(res==float('inf')):
        return 0
    return res




nums = [1,2,3,4,5]
target =11
print(minSize(nums,target))




























# arr=[]

# low=0
# high=low+1
# sum=0

# for i in range(low,high+1):
#     if(nums[i]==target):
#         arr.append(nums[i])
#         if(arr[0]==target):
#             print(arr)
#             break
#     sum=sum+nums[i]

# while(high<len(nums)):
#     if(nums[low]+nums[high]>=target):
#         arr.append(nums[low])
#         arr.append(nums[high])
#         break
#     low+=1
#     high+=1
#     if(high==len(nums)):
#         break
#     sum=sum-nums[low-1]
#     sum=sum+nums[high]
# if(len(arr)==0):
#     print("0")
# print(arr)