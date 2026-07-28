# a = [1,1,2]

# b=1
# count=1

# for i in range(1,len(a)):
#     if(a[i]!=a[i-1]):
#         a[b]=a[i]
#         b+=1
#         count+=1
#         print(a)
# print(count)







# a=[1,1,2]
# a=[0,0,1,1,1,2,2,3,3,4]


# j=1

# count=1

# for i in range(1,len(a)):
#     if(a[i]!=a[i-1]):
#         a[j]=a[i]
#         j+=1
#         count+=1
#         print(a)

# print(count)



# revision i solve correct
nums = [0,0,1,1,1,2,2,3,3,4]

j=1
count=1
for i in range(1,len(nums)):
    if(nums[i]!=nums[i-1]):
        nums[j]=nums[i]
        j+=1
        count+=1
        print(nums)
# print(nums)
print(count)









