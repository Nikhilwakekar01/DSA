nums = [10,5,2,6]
k = 100

low=0
high=0
res=0
product=1

for high in range(len(nums)):
    product=product*nums[high]
    while(product>=k):
        product=product//nums[low]
        low+=1
    length=high-low+1
    res=res+length

print(res)
   

            




    



