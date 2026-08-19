def fun(n):
    sum=0
    while(n>0):
        print("n=",n)
        
        d=n%10
        print("d=",d)
        n=n//10
        print("n= ",n)
       
        sum=sum+d*d
        print("sum",sum)
        
    return sum

def happy(n):
    slow=n
    fast=n
    while(fast!=1):
        slow=fun(slow)
        print("slow= ",slow)
        fast=fun(fast)
        print("fast= ",fast)
        fast=fun(fast)
        print("fast= ",fast)
        if(slow==fast and slow!=1):
            return False
    return True

print(happy(2))