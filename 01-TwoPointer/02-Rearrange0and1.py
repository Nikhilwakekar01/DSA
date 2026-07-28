# a=[1,0,1,0,0,1,1,0]
# n=len(a)
# i=0
# j= n-1   

# while(i<j):
#     if(a[i]==0 and a[j]==1):
#         i+=1
#     elif(a[i]==1 and a[j]==0):
#         temp=a[i]
#         a[i]=a[j]
#         a[j]=temp
#         i+=1
#         j-=1
#     elif(a[i]==0 and a[j]==0):
#         i+=1
#     elif(a[i]==1 and a[j]==1):
#         j-=1

# print(a)
















# revision

# arr=[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

# i=0
# j=len(arr)-1



# while(i<=j):
    
#     if(arr[i]==0 and arr[j]==1):
#         i+=1
#     elif(arr[i]==1 and arr[j]==1):
#         j-=1
#     elif(arr[i]==0 and arr[j]==0):
#         i+=1
#     elif(arr[i]==1 and arr[j]==0):
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1

# print(arr)




arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]

i=0
j=len(arr)-1

while(i<=j):
    
    if(arr[i]==0 and arr[j]==1):
        print(i,j)
        i+=1
        print(arr)
        
    elif(arr[i]==1 and arr[j]==1):
        print(i,j)
        
        j-=1
        print(arr)
       
    elif(arr[i]==0 and arr[j]==0):
        print(i,j)
        i+=1
        print(arr)
        
    elif(arr[i]==1 and arr[j]==0):
        print(i,j)
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
        
        print(arr)
        

# while(i<=j):
#     print("he;lo")
#     if(arr[i]==0 and arr[j]==1):
#         i+=1
#     elif(arr[i]==1 and arr[j]==1):
#         j-=1
#     elif(arr[i]==0 and arr[j]==0):
#         i+=1
#     elif(arr[i]==1 and arr[j]==0):
#         temp=arr[i]
#         arr[i]=arr[j]
#         arr[j]=temp
#         i+=1
#         j-=1

print(arr)
        

# print(arr)