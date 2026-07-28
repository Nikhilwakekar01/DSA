# nums = [-4,-1,0,3,10]

# a=[]
# b=[]

# for i in (nums):
#     if(i<0):
#         a.append(i)
#     else:
#         b.append(i)

# for i in range(len(a)):
#     a[i]=a[i]*a[i]

# for i in range(len(b)):
#     b[i]=b[i]*b[i]
    
# a.reverse()

# i=0
# j=0
# k=0
# res=[]
# while(i<len(a) and j<len(b)):
#     if(a[i]>b[j]):
#         res.append(b[j])
#         j+=1
#     else:
#         res.append(a[i])
#         i+=1
# print(i)
# print(j)

# while(i<len(a)):
#     res.append(a[i])
#     i+=1
# while(j<len(b)):
#     res.append(b[j])
#     j+=1

# print(res)








a = [-4,-1,0,3,10]
neg=[]
pos=[]

for i in range(len(a)):
    if(a[i]<0):
        neg.append(a[i]*a[i])
    else:
        pos.append(a[i]*a[i])
neg.reverse()
s=[]
k=0
i=0
j=0

while(i<len(neg) and j<len(pos)):
    if(neg[i]>pos[j]):
        s.append(pos[i])
        j+=1
    elif(neg[i]<pos[j]):
        s.append(neg[i])
        i+=1

if(i!=len(neg)):
    s.append(neg[i])
    i+=1
elif(j!=len(pos)):
    s.append(pos[j])
    j+=1


print(s)















