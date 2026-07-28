nums=[686, 28, 455, 675, 605, 29, 942, 48, 502, 889, 854, 206, 231, 796, 272, 565, 887, 969, 558, 13, 22, 455, 145, 804, 15]
k=515854

res=[]
# for i in nums:
#     if(i<k):
#         res.append(i)
        

i=0
j=1
res2=[]
while(j<len(nums)):
   
    if(nums[i]*nums[j]<k):
        # print(nums[i],nums[j])
        res.append([nums[i],nums[j]])
        i+=1
        j+=1
print(res)

# p=0
# q=1
# r=2

# while(r<len(nums)):
#     if(nums[p]*nums[q]*nums[r]<k):
#         # print(nums[p],nums[q],nums[r])
#         res.append([nums[p],nums[q],nums[r]])
#         p+=1
#         q+=1
#         r+=1
#     else:
#         p+=1
#         q+=1
#         r+=1


# print(res)
# print(len(res))