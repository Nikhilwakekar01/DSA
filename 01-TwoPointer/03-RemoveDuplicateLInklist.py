a = [1,1,2,3,3]

b=1
count=1

for i in range(1,len(a)):
    if(a[i]!=a[i-1]):
        a[b]=a[i]
        b+=1
        count+=1
    
print(a)
# for i in a:
    

# a[0]=3
# print(a)