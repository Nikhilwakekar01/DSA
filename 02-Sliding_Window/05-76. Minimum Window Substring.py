# solved with array using asscii values
# s = "a"
# t = "aa"


# def sahi(needed,have):
#     for i in range(256):
#         if(have[i]<needed[i]):
#             return False
    
#     return True

# low=0
# high=0
# have=[0]*256
# needed=[0]*256
# res=float("inf")
# start=-1


# for i in range(len(t)):
#     needed[ord(t[i])]+=1



# for high in range(len(s)):
#     have[ord(s[high])]+=1

#     while(sahi(needed,have)):
#         # print("me ander hu")
#         length=high-low+1
#         # print("length:- ",length)
#         if(res>length):
#             res=length
#             start=low
#             print("start :",start)
#         have[ord(s[low])]-=1
#         low+=1
# if(res==float('inf')):
#     print('null')
# print("substring",s[start:start+res])




# soolved with hashmap 
   
s = "ADOBECODEBANC"
t='ABC'

low =0
high=0
have={}
need={}
res=float('inf')
start=-1

for i in range(len(t)):
    need[t[i]]=need.get(t[i],0)+1

def compare(have,need):
    for key in need:
        if have.get(key,0) < need[key]:
            return False
    return True


for high in range(len(s)):
    have[s[high]]=have.get(s[high],0)+1

    while(compare(have,need)):
        length=high-low+1
        
        if(res>length):
            res=length
            start=low
        have[s[low]]-=1
        low+=1
if(res==float('inf')):
    print('null')

print(s[start:start+res])

      

    
    
    
        