# n=[2,7,11,15]
# target=9
# i=0
# j=len(n)-1
# while(i<j):
#     if(n[i]+n[j]==target):
#         print(i+1,j+1)
#         break
#     elif(n[i]+n[j]<target):
#         i+=1
#     elif(n[i]+n[j]>target):
#         j-=1
#     else:
#         print("error")




# numbers = [2,7,11,15,1,23,6]
# target = 9

# i=0
# j=len(numbers)-1

# while(i<j):
#     if(numbers[i]+numbers[j]==target):
#         print(i+1,j+1)
#         break
#     elif(numbers[i]+numbers[j]>target):
#         j-=1
#     elif(numbers[i]+numbers[j]<target):
#         i+=1




numbers = [2,7,11,15]
target = 9

i=0
j=len(numbers)-1

while(i<j):
    if(numbers[i]+numbers[j]==target):
        print(i,j)
        break
    elif(numbers[i]+numbers[j]>target):
        j-=1
    elif(numbers[i]+numbers[j]<target):
        i+=1
    else:
        print("no num found = target")
