s = "aabacbebebe"
k = 3

freq={}
res=-1
low=0
high=0
for high in range(len(s)):
    freq[s[high]]=freq.get(s[high],0)+1
    while(len(freq)>k):
        freq[s[low]]-=1
        if(freq[s[low]]==0):
            del freq[s[low]]
        low+=1
    if(len(freq)==k):
        length=high-low+1
        res=max(length,res)

print(res)

    
