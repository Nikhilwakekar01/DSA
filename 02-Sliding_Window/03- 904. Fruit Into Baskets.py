def function(s):
    freq={}
    res=0
    low=0
    high=0
    for high in range(len(s)):
        freq[s[high]]=freq.get(s[high],0)+1
        while(len(freq)>2):
            freq[s[low]]-=1
            if(freq[s[low]]==0):
                del freq[s[low]]
            low+=1
    length=high-low+1
    res=max(length,res)
    return res


s=[1,2,1]

print(function(s))

