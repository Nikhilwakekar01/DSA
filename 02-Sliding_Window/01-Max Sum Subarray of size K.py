arr =  [100, 200, 300, 400]
k = 2

low=0
high=k-1
sum=0
res=0
for i in range(low,high+1):
    sum=sum+arr[i]

while(high<len(arr)):
    res=max(res,sum)
    low+=1
    high+=1
    if(high==len(arr)):
        break
    sum=sum-arr[low-1]
    sum=sum+arr[high]

print(res)

