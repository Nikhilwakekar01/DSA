nums = [1,1,1,1,1,1,1,1]
target = 11

low=0
high=0
res=float('inf')
sum=0

for high in range(len(nums)):
    sum+=nums[high]
    print("sum chi 1st value:- ",sum)
    while(sum>=target):
        print("sum chi value target peksha mothi ahe")
        length=high-low+1
        print("length :- ",length)
        res=min(length,res)
        print('res chi value:- ',res)
        sum=sum-nums[low]
        print("sum chi dusri value:- ",sum)
        low+=1
        print("low chi value",low)

if(res==float('inf')):
    print('0')

print(res)